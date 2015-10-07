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
      templateUrl: 'app/pubmed/pubmed-list.html',
      controller: 'PubmedListController',
      controllerAs: 'vm'
    })
    .state('pubmed.new', {
      url: 'new/',
      templateUrl: 'app/pubmed/pubmed-form.html',
      controller: 'PubmedFormController',
      controllerAs: 'vm'
    })
    .state('pubmed.edit', {
      url: '{id}/edit/',
      templateUrl: 'app/pubmed/pubmed-form.html',
      controller: 'PubmedFormController',
      controllerAs: 'vm',
      resolve: {
        options: /*@ngInject*/ Restangular => Restangular.all('pubmed')
          .options()
          .then(options => options)
      }
    })
    .state('pubmed.item', {
      url: '{id}/',
      templateUrl: 'app/pubmed/pubmed-list.html',
      controller: 'PubmedListController',
      controllerAs: 'vm'
    });
}

export default routerConfig;
