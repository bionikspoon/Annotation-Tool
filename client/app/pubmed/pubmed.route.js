function routerConfig($stateProvider) {
  'ngInject';
  $stateProvider
    .state('pubmed', {
      url: '',
      abstract: 'true',
      parent: 'main',
      template: '<ui-view/>'
    })
    .state('pubmed.list', {
      url: '',
      templateUrl: 'app/pubmed/list/pubmedList.html',
      controller: 'PubmedListController',
      controllerAs: 'vm'
    })
    .state('pubmed.new', {
      url: 'new/',
      templateUrl: 'app/pubmed/form/pubmedForm.html',
      controller: 'PubmedFormController',
      controllerAs: 'vm',
      resolve: {optionsPrepService}
    })
    .state('pubmed.edit', {
      url: '{id}/edit/',
      templateUrl: 'app/pubmed/form/pubmedForm.html',
      controller: 'PubmedFormController',
      controllerAs: 'vm',
      resolve: {optionsPrepService}
    })
    .state('pubmed.item', {
      url: '{id}/',
      templateUrl: 'app/pubmed/item/pubmedItem.html',
      controller: 'PubmedItemController',
      controllerAs: 'vm'
    });
}

function optionsPrepService(Restangular) {
  'ngInject';
  return Restangular
    .all('pubmed')
    .options()
    .then(options => options);
}

export default routerConfig;
