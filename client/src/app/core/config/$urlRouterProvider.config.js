(function() {
  'use strict';

  // $urlRouterProvider
  angular
    .module('app.core')
    .config($urlRouterProviderConfig);

  /** @ngInject **/
  function $urlRouterProviderConfig($urlRouterProvider) {
    $urlRouterProvider.rule(appendTrailingSlash);
    $urlRouterProvider.otherwise('/');
  }

  /** @ngInject **/
  function appendTrailingSlash($injector) {
    var $location = $injector.get('$location');
    var path = $location.url();

    if(path.endsWith('/') || path.indexOf('/?') > -1) {
      return path;
    } else if(path.indexOf('?') > -1) {
      return path.replace('?', '/?');
    } else {
      return path + '/';
    }
  }

})();
