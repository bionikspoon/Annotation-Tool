(function() {
  'use strict';

  angular
    .module('app.auth', [
      'ngMessages',
      'ui.router',
      'restangular',
      'satellizer',
      'app.layout',
      'app.user'
    ]);

})();
