(function() {
  'use strict';

  angular
    .module('app', [
      'ngAnimate',
      'ngCookies',
      'ngTouch',
      'ngSanitize',
      'app.auth',
      'app.pubmed',
      'app.main',
      'app.core'
    ]);

})();
