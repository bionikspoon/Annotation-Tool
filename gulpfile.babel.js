import gulp from 'gulp';
import gulpLoadPlugins from 'gulp-load-plugins';
import del from 'del';
import {stream as wiredep} from 'wiredep';
import opn from 'opn';

const $ = gulpLoadPlugins();
const config = {
    'local':       'core_local/static/core/',
    'tmp':         '.tmp/core/',
    'tests':       'tests/spec/',
    'dist':        'core_production/static/core/',
    'dist_static': 'core_production/static/',
    'static':      '{core_local,pubmed}/static/{core,pubmed}/'

};
gulp.task('styles', () => {
    return gulp.src(config.local + 'styles/*.scss')

        .pipe($.plumber())

        .pipe($.sourcemaps.init())

        .pipe($.sass.sync({
            outputStyle:  'expanded',
            precision:    10,
            includePaths: ['.']
        }).on('error', $.sass.logError))

        .pipe($.autoprefixer({browsers: ['last 1 version']}))

        .pipe($.sourcemaps.write())

        .pipe(gulp.dest(config.tmp + 'styles'))

});

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

gulp.task('lint', lint(config.local + 'scripts/**/*.js'));
gulp.task('lint:test', lint(config.tests + '**/*.js', testLintOptions));

gulp.task('scripts', () => {
    return gulp.src(config.local + '*.html')

        .pipe($.useref.assets({
            searchPath: ['.']
        }))

        .pipe($.if('*.js', $.uglify()))

        .pipe(gulp.dest('core_production/static'))


});

gulp.task('html', ['scripts', 'styles'], () => {
    const assets = $.useref.assets({
        searchPath: [
            '.tmp', '.'
        ]
    });

    return gulp.src(config.local + '*.html')

        .pipe(assets)

        .pipe($.if('*.css', $.minifyCss({compatibility: '*'})))

        .pipe($.if('*.css', gulp.dest('core_production/static')));

});

gulp.task('images', () => {
    return gulp.src(config.local + 'images/**/*')

        .pipe($.if(//
            $.if.isFile, $.cache(//
                $.imagemin({
                    progressive: true,
                    interlaced:  true, // don't remove IDs from SVGs, they are
                                       // often used
                    // as hooks for embedding and styling
                    svgoPlugins: [{cleanupIDs: false}]
                })//
            ).on('error', function (err) {
                    console.log(err);
                    this.end();
                })//
        ))

        .pipe(gulp.dest(config.dist + 'images'));
});

gulp.task('fonts', () => {
    return gulp

        .src(require('main-bower-files')({
            filter: '**/*.{eot,svg,ttf,woff,woff2}'
        }).concat(config.local + 'fonts/**/*'))

        .pipe(gulp.dest(config.tmp + 'fonts'))

        .pipe(gulp.dest(config.dist + 'fonts'));
});

//copy all files in source root directory to dist
gulp.task('extras', () => {
    return gulp.src([
        config.local + '*.*', '!' + config.local + '*.html'
    ], {
        dot: true
    })

        .pipe(gulp.dest(config.dist));
});

//delete .tmp/dist and dist directories
gulp.task('clean', del.bind(null, [
    '.tmp', '.sass-cache', config.dist_static
]));

gulp.task('serve', ['build'], () => {

    gulp.watch([
        config.local + '*.html'
    ], ['html']);
    gulp.watch([
        config.local + 'images/**/*', config.tmp + 'fonts/**/*'
    ], ['extras']);

    gulp.watch([config.static + 'scripts/*.js'], ['scripts']);
    gulp.watch(config.static + 'styles/**/*.scss', ['styles']);
    gulp.watch(config.static + 'fonts/**/*', ['fonts']);
    gulp.watch('bower.json', ['wiredep', 'build']);
});

gulp.task('serve:cov', function () {
    $.connect.server({
        root: '.htmlcov',
        port: 8002
    });

    opn('http://localhost:8002');
});

// inject bower components
gulp.task('wiredep', () => {
    gulp.src(config.local + 'styles/*.scss')

        .pipe(wiredep({
            ignorePath: /^(\.\.\/)+/
        }))

        .pipe(gulp.dest(config.local + 'styles'));

    gulp.src(config.local + '*.html')

        .pipe(wiredep({
            exclude:    ['bootstrap-sass'],
            ignorePath: /^(\.\.\/)*\.\./
        }))

        .pipe(gulp.dest(config.local));
});


gulp.task('build', ['lint', 'html', 'images', 'fonts', 'extras'], () => {
    return gulp.src(config.dist + '**/*')

        .pipe($.size({
            title: 'build',
            gzip:  true
        }));
});

gulp.task('default', ['clean'], () => {
    gulp.start('build');
});
