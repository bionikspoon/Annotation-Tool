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

    .pipe($.eslint.format()));
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

    .pipe($.bytediff.start())

    .pipe($.minifyCss())

    .pipe(gulp.dest(config.dist('styles')))

    .pipe($.gzip(gzip_options))

    .pipe($.bytediff.stop())

    .pipe(gulp.dest(config.dist('styles')))

    .pipe($.livereload()));
const buildScripts = function (srcPath, dist, name) {
    gulp

        .src(srcPath)

        //.pipe($.debug({title: name}))

        .pipe($.plumber())

        .pipe($.bytediff.start())

        .pipe($.sourcemaps.init())

        .pipe($.concat(name))

        .pipe($.sourcemaps.write(sourcemapOptions))

        .pipe(gulp.dest(dist))

        .pipe($.rename({suffix: '.min'}))

        .pipe($.uglify())

        .pipe(gulp.dest(dist))

        .pipe($.gzip(gzip_options))

        .pipe($.bytediff.stop())

        .pipe(gulp.dest(dist))

        .pipe($.livereload());
};
gulp.task('scripts',
    buildScripts(config.src('scripts/*.js'),
        config.dist('scripts'),
        'main.js'));
gulp.task('scripts:vendor',
    buildScripts($.mainBowerFiles('**/*.js'),
        config.dist('scripts'),
        'vendor.js'));

// don't remove IDs from SVGs, they are often used as hooks for embedding and
// styling
const imageminOptions = {
    progressive: true,
    interlaced:  true,
    svgoPlugins: [{cleanupIDs: false}]
};
gulp.task('images', () => {
    const local = gulp.src(config.src('images/*'));
    const bower = gulp.src($.mainBowerFiles('**/{img,images}/**/*.{png,svg}'));

    return $.mergeStream(local, bower)

        .pipe($.plumber())

        .pipe($.bytediff.start())

        .pipe($.if($.if.isFile, $.cache($.imagemin(imageminOptions))

            .on('error', function (err) {
                console.log(err);
                this.end();
            })))

        .pipe($.bytediff.stop())

        .pipe(gulp.dest(config.dist('images')))

});
gulp.task('watch', () => {
    $.livereload.listen();
    gulp.watch(config.src('styles/*.scss'), ['lint', 'styles']);
    gulp.watch(config.src('scripts/*.js'), ['lint', 'scripts']);
    gulp.watch(config.root('bower.json'), ['scripts:vendor']);
    gulp.watch('**/templates/*').on('change', $.livereload.changed)
});
gulp.task('build', [
    'clean', 'styles', 'scripts', 'scripts:vendor', 'images'
]);
gulp.task('default', ['build', 'watch']);

