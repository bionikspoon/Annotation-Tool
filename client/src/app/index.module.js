(function() {
  'use strict';

  angular
    .module('app', [
      'ngAnimate',
      'ngCookies',
      'ngTouch',
      'ngSanitize',
      /*'ngMaterial',*/
      'app.auth',
      'app.pubmed',
      'app.main',
      'app.core'
    ]);

})();
