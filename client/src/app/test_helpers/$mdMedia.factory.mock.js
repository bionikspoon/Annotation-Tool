(function() {
  'use strict';

  angular
    .module('mock.$mdMedia', [])
    .config(function($provide) {
      $provide.factory('$mdMedia', mock$mdMedia);
    });

  /** @ngInject **/
  function mock$mdMedia() {
    var self = $mdMedia;
    self.return = false;
    return self;

    ////////////////

    function $mdMedia() {
      return self.return;
    }
  }

})();
