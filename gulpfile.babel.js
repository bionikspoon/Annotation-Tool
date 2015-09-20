import gulp from 'gulp';
import gulpLoadPlugins from 'gulp-load-plugins';
import del from 'del';
import {stream as wiredep} from 'wiredep';
import opn from 'opn';

const $ = gulpLoadPlugins({
        pattern: ['gulp-*', 'gulp.*', 'main-bower-files', 'merge-stream']
    }
);
const config = {
    local_static_core: 'core/local/static/core/',
    local_static:      'core/local/static/',
    tmp_core:          '.tmp/core/',
    tests:             'tests/spec/',
    prod_static_core:  'core/production/static/core/',
    prod_static:       'core/production/static/',
    static_glob:       '{core/local,pubmed}/static/{core,pubmed}/'

};

const gzip_options = {
    threshold:   '1kb',
    gzipOptions: {
        level: 9
    }
};

gulp.task('styles', ()=> gulp

        .src('annotation_tool/static/scss/*.scss')

        .pipe($.sass())

        .pipe(gulp.dest('annotation_tool/static/css'))

        .pipe($.rename({suffix: '.min'}))

        .pipe($.minifyCss())

        .pipe(gulp.dest('annotation_tool/static/css'))

        .pipe($.gzip(gzip_options))

        .pipe(gulp.dest('annotation_tool/static/css'))

        .pipe($.livereload())
);

gulp.task('watch', () => {
        $.livereload.listen();
        gulp.watch('annotation_tool/static/scss/*.scss', ['styles']);
        gulp.watch('**/templates/*').on('change', $.livereload.changed)
    }
);
gulp.task('default', ['styles', 'watch']);

