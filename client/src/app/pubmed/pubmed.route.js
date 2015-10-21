(function() {
  'use strict';

  angular
    .module('app.pubmed')
    .config(pubmedRoutes);

  /** @ngInject **/
  function pubmedRoutes($stateProvider) {
    $stateProvider
      .state('pubmed', {
        url:      '',
        abstract: 'true',
        parent:   'main',
        template: '<ui-view ></ui-view>'
      })
      .state('pubmed.list', {
        url:          '',
        templateUrl:  'app/pubmed/list/pubmedList.html',
        controller:   'PubmedListController',
        controllerAs: 'vm'
      });
  }
})();
