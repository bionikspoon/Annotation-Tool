import gulp from 'gulp';
import gulpLoadPlugins from 'gulp-load-plugins';
import del from 'del';
import {stream as wiredep} from 'wiredep';
import opn from 'opn';

const $ = gulpLoadPlugins();
const config = {
    local_static_core: 'core/local/static/core/',
    local_static:      'core/local/static/',
    tmp_core:          '.tmp/core/',
    tests:             'tests/spec/',
    prod_static_core:  'core/production/static/core/',
    prod_static:       'core/production/static/',
    static_glob:       '{core/local,pubmed}/static/{core,pubmed}/'

};
gulp.task('styles', () => {
    return gulp.src(config.local_static_core + 'styles/*.scss')

        .pipe($.plumber())

        .pipe($.sourcemaps.init())

        .pipe($.sass.sync({
            outputStyle:  'expanded',
            precision:    10,
            includePaths: [
                '.',
                'bower_components/flat-ui-sass/vendor/assets/stylesheets/'
            ]
        }).on('error', $.sass.logError))

        .pipe($.autoprefixer({browsers: ['last 1 version']}))

        .pipe($.sourcemaps.write())

        .pipe(gulp.dest(config.tmp_core + 'styles'))


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

gulp.task('lint', lint(config.local_static_core + 'scripts/**/*.js'));
gulp.task('lint:test', lint(config.tests + '**/*.js', testLintOptions));

gulp.task('scripts', () => {
    return gulp.src(config.local_static + '*.html')

        .pipe($.useref.assets({
            searchPath: [config.local_static, 'pubmed/static/', '.']
        }))

        .pipe($.if('*.js', $.uglify()))

        .pipe(gulp.dest(config.prod_static))


});

gulp.task('html', ['scripts', 'styles'], () => {
    const assets = $.useref.assets({
        searchPath: ['.tmp/', config.local_static, 'pubmed/static/', '.']
    });

    return gulp.src(config.local_static + '*.html')

        .pipe(assets)

        .pipe($.if('*.css', $.minifyCss({compatibility: '*'})))

        .pipe($.if('*.css', gulp.dest(config.prod_static)));

});

gulp.task('images', () => {
    return gulp.src(config.local_static_core + 'images/**/*')

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

        .pipe(gulp.dest(config.prod_static_core + 'images'));
});

gulp.task('fonts', () => {
    return gulp

        .src(require('main-bower-files')({
            filter: '**/*.{eot,svg,ttf,woff,woff2}'
        }).concat(config.local_static_core + 'fonts/**/*'))

        .pipe(gulp.dest(config.tmp_core + 'fonts'))

        .pipe(gulp.dest(config.prod_static_core + 'fonts'));
});

//copy all files in source root directory to dist
gulp.task('extras', () => {
    return gulp.src([
            config.local_static_core + '*.*',
            '!' + config.local_static_core + '*.html'
        ],
        {
            dot: true
        })

        .pipe(gulp.dest(config.prod_static_core));
});

//delete .tmp/dist and dist directories
gulp.task('clean', del.bind(null, [
    '.tmp', '.sass-cache', config.prod_static
]));

gulp.task('serve', ['build'], () => {

    gulp.watch([
        config.local_static_core + '*.html'
    ], ['html']);
    gulp.watch([
        config.local_static_core + 'images/**/*', config.tmp_core + 'fonts/**/*'
    ], ['extras']);

    gulp.watch([config.static_glob + 'scripts/*.js'], ['scripts']);
    gulp.watch(config.static_glob + 'styles/**/*.scss', ['styles']);
    gulp.watch(config.static_glob + 'fonts/**/*', ['fonts']);
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
    gulp.src(config.local_static_core + 'styles/*.scss')

        .pipe(wiredep({
            ignorePath: /^(\.\.\/)+/
        }))

        .pipe(gulp.dest(config.local_static_core + 'styles'));


    gulp.src(config.local_static + '*.html')

        .pipe(wiredep({
            exclude:    ['bootstrap-sass'],
            ignorePath: /^(\.\.\/)*\.\./
        }))

        .pipe(gulp.dest(config.local_static));
});


gulp.task('build', [
    'wiredep', 'lint', 'html', 'images', 'fonts', 'extras'
], () => {
    return gulp.src(config.prod_static_core + '**/*')

        .pipe($.size({
            title: 'build',
            gzip:  true
        }));
});

gulp.task('default', ['clean'], () => {
    gulp.start('build');
});
