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
      })
      .state('pubmed.edit', {
        url:          '{id}/edit/',
        templateUrl:  'app/pubmed/form/pubmedForm.html',
        controller:   'PubmedFormController',
        controllerAs: 'vm'
      })
      .state('pubmed.new', {
        url:          'new/',
        templateUrl:  'app/pubmed/form/pubmedForm.html',
        controller:   'PubmedFormController',
        controllerAs: 'vm'
      })
      .state('pubmed.item', {
        url:          '{id}/',
        templateUrl:  'app/pubmed/item/pubmedItem.html',
        controller:   'PubmedItemController',
        controllerAs: 'vm'
      });
  }
})();
