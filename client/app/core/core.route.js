function routerConfig($stateProvider) {
  'ngInject';
  $stateProvider
    .state('core', {
      url: '/',
      templateUrl: 'app/core/core.html',
      controller: 'CoreController',
      controllerAs: 'main',
      abstract: true
    });

}

export default routerConfig;
