(function() {
  'use strict';

  angular
    .module('app.main')
    .config(mainRoutes);

  /** @ngInject **/
  function mainRoutes($stateProvider) {
    $stateProvider
      .state('main', {
        url:          '/',
        templateUrl:  'app/main/main.html',
        controller:   'MainController',
        controllerAs: 'vm',
        abstract:     true
      })
      .state('pubmed', {
        url:      '',
        parent:   'main',
        template: '<h1>Hello</h1>'
      });
  }
})();
