// generated on 2015-08-28 using generator-gulp-webapp 1.0.3
import gulp from 'gulp';
import gulpLoadPlugins from 'gulp-load-plugins';
import del from 'del';
import {stream as wiredep} from 'wiredep';

const $ = gulpLoadPlugins();

gulp.task('styles', () => {
  return gulp.src('core/static/source/styles/*.scss')

    .pipe($.plumber())

    .pipe($.sourcemaps.init())

    .pipe($.sass.sync({
      outputStyle:  'expanded',
      precision:    10,
      includePaths: ['.']
    }).on('error', $.sass.logError))

    .pipe($.autoprefixer({browsers: ['last 1 version']}))

    .pipe($.sourcemaps.write())

    .pipe(gulp.dest('.tmp/dist/styles'))

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

gulp.task('lint', lint('core/static/source/scripts/**/*.js'));
gulp.task('lint:test', lint('tests/spec/**/*.js', testLintOptions));

gulp.task('scripts', () => {
  return gulp.src('core/static/source/*.html')

    .pipe($.useref.assets({
      searchPath: ['.']
    }))

    .pipe($.if('*.js', $.uglify()))

    .pipe(gulp.dest('core/static'))


});

gulp.task('html', ['scripts', 'styles'], () => {
  const assets = $.useref.assets({
    searchPath: [
      '.tmp', '.'
    ]
  });

  return gulp.src('core/static/source/*.html')

    .pipe(assets)

    .pipe($.if('*.css', $.minifyCss({compatibility: '*'})))

    .pipe($.if('*.css', gulp.dest('core/static')));

});

gulp.task('images', () => {
  return gulp.src('core/static/source/images/**/*')

    .pipe($.if(//
      $.if.isFile, $.cache(//
        $.imagemin({
          progressive: true,
          interlaced:  true, // don't remove IDs from SVGs, they are often used
          // as hooks for embedding and styling
          svgoPlugins: [{cleanupIDs: false}]
        })//
      ).on('error', function (err) {
          console.log(err);
          this.end();
        })//
    ))

    .pipe(gulp.dest('core/static/dist/images'));
});

gulp.task('fonts', () => {
  return gulp

    .src(require('main-bower-files')({
      filter: '**/*.{eot,svg,ttf,woff,woff2}'
    }).concat('core/static/source/fonts/**/*'))

    .pipe(gulp.dest('.tmp/dist/fonts'))

    .pipe(gulp.dest('core/static/dist/fonts'));
});

//copy all files in source root directory to dist
gulp.task('extras', () => {
  return gulp.src([
    'core/static/source/*.*', '!core/static/source/*.html'
  ], {
    dot: true
  })

    .pipe(gulp.dest('core/static/dist'));
});

//delete .tmp/dist and dist directories
gulp.task('clean', del.bind(null, [
  '.tmp', '.sass-cache', 'core/static/dist', 'core/static/pubmed'
]));

gulp.task('serve', ['build'], () => {

  gulp.watch([
    'core/static/source/*.html'
  ], ['html']);
  gulp.watch([
    'core/static/source/images/**/*', '.tmp/dist/fonts/**/*'
  ], ['extras']);

  gulp.watch(['{core,pubmed}/static/{source,pubmed}/scripts/*.js'],
    ['scripts']);
  gulp.watch('{core,pubmed}/static/{source,pubmed}/styles/**/*.scss',
    ['styles']);
  gulp.watch('{core,pubmed}/static/{source,pubmed}/fonts/**/*', ['fonts']);
  gulp.watch('bower.json', ['wiredep', 'build']);
});


// inject bower components
gulp.task('wiredep', () => {
  gulp.src('core/static/source/styles/*.scss')

    .pipe(wiredep({
      ignorePath: /^(\.\.\/)+/
    }))

    .pipe(gulp.dest('core/static/source/styles'));

  gulp.src('core/static/source/*.html')

    .pipe(wiredep({
      exclude:    ['bootstrap-sass'],
      ignorePath: /^(\.\.\/)*\.\./
    }))

    .pipe(gulp.dest('core/static/source'));
});

gulp.task('build', ['lint', 'html', 'images', 'fonts', 'extras'], () => {
  return gulp.src('core/static/dist/**/*')

    .pipe($.size({
      title: 'build',
      gzip:  true
    }));
});

gulp.task('default', ['clean'], () => {
  gulp.start('build');
});
