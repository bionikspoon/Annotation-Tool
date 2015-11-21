'use strict';

var path = require('path');
var gulp = require('gulp');
var karma = require('karma');

function runTests(singleRun, done) {
  var serverConfig = {
    configFile: path.join(__dirname, '/../karma.conf.js'),
    singleRun:  singleRun,
    autoWatch:  !singleRun
  };

  var server = new karma.Server(serverConfig, function() {done();});
  server.start();
}

gulp.task('test', ['scripts'], function(done) {runTests(true, done);});

gulp.task('test:auto', ['watch'], function(done) {runTests(false, done);});
