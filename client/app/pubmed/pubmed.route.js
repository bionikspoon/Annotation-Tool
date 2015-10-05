function routerConfig($stateProvider) {
  'ngInject';

  $stateProvider
    .state('pubmed', {
      url:          '/',
      templateUrl:  'app/main/main.html',
      controller:   'MainController',
      controllerAs: 'main',
      abstract:     'true'
    })
    .state('pubmed.list', {
      url:          '',
      templateUrl:  'app/pubmed/pubmed-list.html',
      controller:   'PubmedListController',
      controllerAs: 'vm'
    })
    .state('pubmed.new', {
      url:          'new',
      templateUrl:  'app/pubmed/pubmed-form.html',
      controller:   'PubmedFormController',
      controllerAs: 'vm'
    })
    .state('pubmed.item', {
      url:          '{id}',
      templateUrl:  'app/pubmed/pubmed-list.html',
      controller:   'PubmedListController',
      controllerAs: 'vm'
    })
    .state('pubmed.edit', {
      url:          '{id}/edit',
      templateUrl:  'app/pubmed/pubmed-form.html',
      controller:   'PubmedFormController',
      controllerAs: 'vm'
    });
}

export default routerConfig;
