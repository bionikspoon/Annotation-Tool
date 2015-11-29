'use strict';

var path = require('path');
var gulp = require('gulp');
var conf = require('./conf');

var $ = require('gulp-load-plugins')({
  pattern: [
    'gulp-*',
    'main-bower-files',
    'uglify-save-license',
    'del'
  ]
});

gulp.task('partials', taskPartials);

gulp.task('html', [
  'inject',
  'partials'
], taskHtml);

gulp.task('images', taskImages);

// Only applies for fonts from bower dependencies
// Custom fonts are handled by the "other" task
gulp.task('fonts', taskFonts);

gulp.task('other', taskOther);

gulp.task('clean', taskClean);

gulp.task('copy', taskCopy);

gulp.task('build', [
  'html',
  'images',
  'fonts',
  'other'
], function() {return gulp.start('copy');});

function taskPartials() {
  //noinspection JSUnresolvedFunction
  return gulp
    .src([
      path.join(conf.paths.src, '/app/**/*.html'),
      path.join(conf.paths.tmp, '/serve/app/**/*.html')
    ])
    .pipe($.minifyHtml({
      empty:  true,
      spare:  true,
      quotes: true
    }))
    .pipe($.angularTemplatecache('templateCacheHtml.js', {
      module: 'app',
      root:   'app'
    }))
    .pipe(gulp.dest(conf.paths.tmp + '/partials/'));
}
function taskImages() {
  //noinspection JSUnresolvedFunction
  return gulp
    .src(path.join(conf.paths.src, '/assets/images/**/*'))
    .pipe($.imagemin({
      optimizationLevel: 3,
      progressive:       true,
      interlaced:        true
    }))
    .pipe(gulp.dest(path.join(conf.paths.dist, '/assets/images/')));
}

function taskFonts() {
  //noinspection JSUnresolvedFunction
  return gulp
    .src($.mainBowerFiles())
    .pipe($.filter('**/*.{eot,svg,ttf,woff,woff2}'))
    .pipe($.flatten())
    .pipe(gulp.dest(path.join(conf.paths.dist, '/fonts/')));
}

function taskOther() {
  var fileFilter = $.filter(function(file) {
    return file.stat.isFile();
  });

  return gulp
    .src([
      path.join(conf.paths.src, '/**/*'),
      path.join('!' + conf.paths.src, '/**/*.{html,css,js,scss,jpg,png,gif,svg}')
    ])
    .pipe(fileFilter)
    .pipe(gulp.dest(path.join(conf.paths.dist, '/')));
}

function taskClean() {
  //noinspection JSUnresolvedFunction
  $.del([
    path.join(conf.paths.server, '/'),
    path.join(conf.paths.dist, '/'),
    path.join(conf.paths.tmp, '/')
  ], {force: true});
}

function taskHtml() {
  var partialsInjectFile = gulp.src(path.join(conf.paths.tmp, '/partials/templateCacheHtml.js'), {read: false});
  var partialsInjectOptions = {
    starttag:     '<!-- inject:partials -->',
    ignorePath:   path.join(conf.paths.tmp, '/partials'),
    addRootSlash: false
  };

  var htmlFilter = $.filter('*.html', {restore: true});
  var jsFilter = $.filter('**/*.js', {restore: true});
  var cssFilter = $.filter('**/*.css', {restore: true});
  //var assets; // --

  //noinspection JSUnresolvedFunction,JSUnresolvedVariable
  return gulp
    .src(path.join(conf.paths.tmp, '/serve/*.html'))
    .pipe($.inject(partialsInjectFile, partialsInjectOptions))
    .pipe($.useref()) // ++
    //.pipe(assets = $.useref.assets()) // --
    .pipe($.rev())
    .pipe(jsFilter)
    .pipe($.ngAnnotate())
    .pipe($.uglify({preserveComments: $.uglifySaveLicense})).on('error', conf.errorHandler('Uglify'))
    .pipe(jsFilter.restore)
    .pipe(cssFilter)
    .pipe($.csso())
    .pipe(cssFilter.restore)
    //.pipe(assets.restore()) // --
    //.pipe($.useref()) // --
    .pipe($.revReplace())
    .pipe(htmlFilter)
    .pipe($.minifyHtml({
      empty:        true,
      spare:        true,
      quotes:       true,
      conditionals: true
    }))
    .pipe(htmlFilter.restore)
    .pipe(gulp.dest(path.join(conf.paths.dist, '/')))
    .pipe($.size({
      title:     path.join(conf.paths.dist, '/'),
      showFiles: true
    }));
}

function taskCopy() {
  return gulp
    .src(path.join(conf.paths.dist, '/**/*'))
    .pipe(gulp.dest(path.join(conf.paths.server, '/')));
}
