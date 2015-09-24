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
  const root = _.partial(path.join, path.dirname('.'));
  const apps = _.partial(path.join, root('annotation_tool'));
  const src = _.partial(path.join, apps('static'));
  const dist = _.partial(path.join, root('dist'));
  return {
                      root,
                      apps,
                      src,
                      dist,
    gzipOptions:      {
      threshold:   '1kb',
      gzipOptions: {
        level: 9
      }
    },
    sassOptions:      {

      outputStyle:  'expanded',
      precision:    10,
      includePaths: [
        root(), root('bower_components/bootstrap-sass/assets/stylesheets/')
      ]
    },
    sourcemapOptions: {
      includeContent: false,
      sourceRoot:     src()
    },
    imageminOptions:  {
      progressive: true,
      interlaced:  true,
      svgoPlugins: [{cleanupIDs: false}]
    },
    userefOptions:    {
      searchPath: [root(), src()]
    },
    uglifyOptions:    {
      preserveComments: 'license'
    },
    wiredepOptions:   {
      ignorePath: /^(\.\.\/)+/,
      fileTypes:  {
        html: {
          detect:  {
            less:  /<link.*href=['"]([^'"]+)/gi,
            sass:  /<link.*href=['"]([^'"]+)/gi,
            scss:  /<link.*href=['"]([^'"]+)/gi,
            style: /<link.*href=['"]([^'"]+)/gi
          },
          replace: {
            less:  '<link href="{{filePath}}" />',
            sass:  '<link href="{{filePath}}" />',
            scss:  '<link href="{{filePath}}" />',
            style: '<link href="{{filePath}}" />'
          }
        }
      }

    }
  }
})();


gulp.task('clean', () => $.del([config.dist()]));

function lint(files, options) {
  return () => {
    return gulp.src(files)


      .pipe($.eslint(options))

      .pipe($.eslint.format())

  };
}

gulp.task('lint', () => gulp

  .src(config.src('scripts/**/*.js'))

  .pipe($.eslint())

  .pipe($.eslint.format())//
);

gulp.task('wiredep', () => gulp

  .src(config.src('manifest.html'))

  .pipe(wiredep(config.wiredepOptions))

  .pipe(gulp.dest(config.src()))//


);
gulp.task('styles', ()=> gulp

  .src(config.src('styles/*.scss'))

  .pipe($.plumber())

  .pipe($.sourcemaps.init())

  .pipe($.sass.sync(config.sassOptions).on('error', $.sass.logError))

  .pipe($.autoprefixer({browsers: ['last 2 version']}))

  .pipe($.sourcemaps.write('.', config.sourcemapOptions))

  .pipe(gulp.dest(config.dist('styles')))

  .pipe($.rename({suffix: '.min'}))

  .pipe($.bytediff.start())

  .pipe($.minifyCss())

  .pipe($.bytediff.stop())

  .pipe(gulp.dest(config.dist('styles')))

  .pipe($.bytediff.start())

  .pipe($.gzip(config.gzipOptions))

  .pipe($.bytediff.stop())

  .pipe(gulp.dest(config.dist('styles')))

  .pipe($.livereload())//
);

gulp.task('styles:vendor', ()=> gulp

  .src(config.src('manifest.html'))

  .pipe($.plumber())

  .pipe($.useref.assets(config.userefOptions))

  .pipe($.filter('**/*.css'))

  .pipe($.sourcemaps.init())

  .pipe(gulp.dest(config.dist()))

  .pipe($.sourcemaps.write('.', config.sourcemapOptions))

  .pipe($.rename({suffix: '.min'}))

  .pipe($.bytediff.start())

  .pipe($.minifyCss())

  .pipe($.bytediff.stop())

  .pipe(gulp.dest(config.dist()))

  .pipe($.bytediff.start())

  .pipe($.gzip(config.gzipOptions))

  .pipe($.bytediff.stop())

  .pipe(gulp.dest(config.dist()))

  .pipe($.livereload())//
);


gulp.task('scripts', () => gulp

  .src(config.src('manifest.html'))

  .pipe($.plumber())

  //.pipe($.debug({title: 'manifest'}))

  .pipe($.useref.assets(config.userefOptions))

  //.pipe($.debug({title: 'assets'}))

  .pipe($.filter('**/*.js'))

  .pipe($.bytediff.start())

  .pipe($.sourcemaps.init())

  .pipe(gulp.dest(config.dist()))

  .pipe($.rename({suffix: '.min'}))

  .pipe($.uglify(config.uglifyOptions))

  .pipe($.bytediff.stop())

  .pipe($.sourcemaps.write('.', config.sourcemapOptions))

  .pipe(gulp.dest(config.dist()))

  .pipe($.bytediff.start())

  .pipe($.gzip(config.gzipOptions))

  .pipe($.bytediff.stop())

  .pipe(gulp.dest(config.dist()))

  .pipe($.livereload())//
);

// don't remove IDs from SVGs, they are often used as hooks for embedding and
// styling
gulp.task('images', () => {
  const local = gulp.src(config.src('images/*'));
  const bower = gulp.src($.mainBowerFiles('**/{img,images}/**/*.{png,svg}'));

  return $.mergeStream(local, bower)

    .pipe($.plumber())

    .pipe($.bytediff.start())

    .pipe($.if($.if.isFile, $.cache($.imagemin(config.imageminOptions))

      .on('error', function (err) {
        console.log(err);
        this.end();
      })))

    .pipe($.bytediff.stop())

    .pipe(gulp.dest(config.dist('images')))

});

gulp.task('clean:cov', () => $.del([config.root('.htmlcov')]));

gulp.task('serve:cov', () => {
  $.connect.server({
    root: '.htmlcov',
    port: 8002
  });

  opn('http://localhost:8002');

});

gulp.task('watch:project', () => {
  $.livereload.listen();
  gulp.watch(config.src('styles/**/*.scss'), ['styles']);
  gulp.watch(config.src('scripts/**/*.js'), ['scripts']);
  gulp.watch(config.src(config.root('bower.json')), ['scripts']);
  gulp.watch(config.apps('**/*.{py,html}')).on('change', $.livereload.changed)
});

gulp.task('build:project', [
  'styles', 'styles:vendor', 'scripts', 'images'
]);

gulp.task('build', ['clean', 'wiredep'], () => {
  gulp.start('build:project');
});

gulp.task('watch', ['build', 'watch:project']);

gulp.task('default', ['build']);

