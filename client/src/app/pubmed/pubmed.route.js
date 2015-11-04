(function() {
  'use strict';

  angular
    .module('app.pubmed')
    .config(pubmedRoutes);

  /** @ngInject **/
  function pubmedRoutes($stateProvider, PERMISSION) {
    $stateProvider
      .state('pubmed', {
        url:      '',
        abstract: 'true',
        parent:   'main',
        template: '<ui-view></ui-view>'
      })
      .state('pubmed.list', {
        url:          '',
        templateUrl:  'app/pubmed/list/pubmedList.html',
        controller:   'pubmedListController',
        controllerAs: 'vm'
      })
      .state('pubmed.edit', {
        url:          '{id}/edit/',
        templateUrl:  'app/pubmed/form/pubmedForm.html',
        controller:   'pubmedFormController',
        controllerAs: 'vm',
        data:         {
          authenticate: true,
          permission:   PERMISSION.pubmed.change
        }
      })
      .state('pubmed.new', {
        url:          'new/',
        templateUrl:  'app/pubmed/form/pubmedForm.html',
        controller:   'pubmedFormController',
        controllerAs: 'vm',
        data:         {
          authenticate: true,
          permission:   PERMISSION.pubmed.add
        }
      })
      .state('pubmed.item', {
        url:          '{id}/',
        templateUrl:  'app/pubmed/item/pubmedItem.html',
        controller:   'pubmedItemController',
        controllerAs: 'vm'
      });
  }
})();
