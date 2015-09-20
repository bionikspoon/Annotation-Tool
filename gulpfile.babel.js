import gulp from 'gulp';
import gulpLoadPlugins from 'gulp-load-plugins';
import del from 'del';
import {stream as wiredep} from 'wiredep';
import opn from 'opn';
import path from 'path';
import _ from 'lodash';

const $ = gulpLoadPlugins({
        pattern: ['gulp-*', 'gulp.*', 'main-bower-files', 'merge-stream']
    }
);

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
console.log(config.src);

const gzip_options = {
    threshold:   '1kb',
    gzipOptions: {
        level: 9
    }
};

gulp.task('styles', ()=> gulp

        .src(config.src('styles/*.scss'))

        .pipe($.sass())

        .pipe(gulp.dest(config.dist('styles')))

        .pipe($.rename({suffix: '.min'}))

        .pipe($.minifyCss())

        .pipe(gulp.dest(config.dist('styles')))

        .pipe($.gzip(gzip_options))

        .pipe(gulp.dest(config.dist('styles')))

        .pipe($.livereload())
);

gulp.task('watch', () => {
        $.livereload.listen();
        gulp.watch(config.src('styles/*.scss'), ['styles']);
        gulp.watch('**/templates/*').on('change', $.livereload.changed)
    }
);
gulp.task('default', ['styles', 'watch']);

