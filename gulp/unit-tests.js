'use strict';

var path = require('path');
var gulp = require('gulp');
var conf = require('./conf');

var karma = require('karma');

function runTests(singleRun, done) {
  const server = new karma.Server({
    configFile: path.join(__dirname, '/../karma.conf.js'),
    singleRun: singleRun,
    autoWatch: !singleRun
  }, () => done());
  server.start();
  //karma.server.start({
  //  configFile: path.join(__dirname, '/../karma.conf.js'),
  //  singleRun: singleRun,
  //  autoWatch: !singleRun
  //}, function() {
  //  done();
  //});
}

gulp.task('test', ['scripts'], function(done) {
  runTests(true, done);
});

gulp.task('test:auto', ['watch'], function(done) {
  runTests(false, done);
});
