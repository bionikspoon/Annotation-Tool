import gulp from 'gulp';
import gulpLoadPlugins from 'gulp-load-plugins';
import {stream as wiredep} from 'wiredep';
import opn from 'opn';
import path from 'path';
import _ from 'lodash';

const loadPluginOptions = {
    pattern: ['gulp-*', 'gulp.*', 'main-bower-files', 'merge-stream', 'del']
};
const $ = gulpLoadPlugins(loadPluginOptions);

const config = (()=> {
    const root = path.dirname('.');
    const apps = path.join(root, 'annotation_tool');
    const src = path.join(apps, 'static');
    const dist = path.join(root, 'dist');
    return {
        root: _.partial(path.join, root),
        apps: _.partial(path.join, apps),
        src:  _.partial(path.join, src),
        dist: _.partial(path.join, dist)
    }
})();


const gzip_options = {
    threshold:   '1kb',
    gzipOptions: {
        level: 9
    }
};
gulp.task('clean', () => $.del([config.dist('**/*')]));
function lint(files, options) {
    return () => {
        return gulp.src(files)


            .pipe($.eslint(options))

            .pipe($.eslint.format())

    };
}
const testLintOptions = {
    env: {
        mocha: true
    }
};

gulp.task('lint', () => gulp

        .src(config.src('scripts/**/*.js'))

        .pipe($.eslint())

        .pipe($.eslint.format())
);
const sassOptions = {

    outputStyle:  'expanded',
    precision:    10,
    includePaths: [
        config.root(), config.root('bower_components/foundation/scss/')
    ]
};
const sourcemapOptions = {
    includeContent: false,
    sourceRoot:     config.src()
};
gulp.task('styles', ()=> gulp

        .src(config.src('styles/*.scss'))

        .pipe($.plumber())

        .pipe($.sourcemaps.init())

        .pipe($.sass.sync(sassOptions).on('error', $.sass.logError))

        .pipe($.autoprefixer({browsers: ['last 2 version']}))

        .pipe($.sourcemaps.write('.', sourcemapOptions))

        .pipe(gulp.dest(config.dist('styles')))

        .pipe($.rename({suffix: '.min'}))

        .pipe($.minifyCss())

        .pipe(gulp.dest(config.dist('styles')))

        .pipe($.gzip(gzip_options))

        .pipe(gulp.dest(config.dist('styles')))

        .pipe($.livereload())
);
function javascript(srcPath, dist, name) {
    gulp

        .src(srcPath)

        .pipe($.debug({title: name}))

        .pipe($.plumber())

        .pipe($.sourcemaps.init())

        .pipe($.concat(name))

        .pipe($.sourcemaps.write(sourcemapOptions))

        .pipe(gulp.dest(dist))

        .pipe($.rename({suffix: '.min'}))

        .pipe($.uglify())

        .pipe(gulp.dest(dist))

        .pipe($.gzip(gzip_options))

        .pipe(gulp.dest(dist))

        .pipe($.livereload());
}
gulp.task('scripts',
    javascript(config.src('scripts/*.js'), config.dist('scripts'), 'main.js')
);
gulp.task('scripts:vendor',
    javascript($.mainBowerFiles('**/*.js'), config.dist('scripts'), 'vendor.js'
    )
);


gulp.task('watch', () => {
        $.livereload.listen();
        gulp.watch(config.src('styles/*.scss'), ['lint', 'styles']);
        gulp.watch(config.src('scripts/*.js'), ['lint', 'scripts']);
        gulp.watch(config.root('bower.json'), ['scripts:vendor']);
        gulp.watch('**/templates/*').on('change', $.livereload.changed)
    }
);
gulp.task('build', [
        'clean', 'styles', 'scripts', 'scripts:vendor'
    ]
);
gulp.task('default', ['build', 'watch']);

