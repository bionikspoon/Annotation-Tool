function routerConfig($stateProvider, $urlRouterProvider) {
  'ngInject';
  $stateProvider
    .state('main', {
      url:          '/',
      templateUrl:  'app/main/main.html',
      controller:   'MainController',
      controllerAs: 'main',
      abstract:     'true'
    });

  $urlRouterProvider.otherwise('/');
}

export default routerConfig;
