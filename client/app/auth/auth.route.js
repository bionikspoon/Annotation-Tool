function routerConfig($stateProvider) {
  'ngInject';
  $stateProvider
    .state('auth', {
      url: 'auth/',
      abstract: 'true',
      parent: 'main',
      template: '<ui-view/>'
    })
    .state('auth.login', {
      url: 'login/',
      controller: 'AuthLoginController',
      controllerAs: 'vm',
      templateUrl: 'app/auth/login/authLogin.html'

    })
    .state('auth.logout', {
      url: 'logout/',
      controller: 'AuthLoginController',
      controllerAs: 'vm',
      templateUrl: 'app/auth/login/authLogin.html'

    })
    .state('auth.register', {
      url: 'register/',
      controller: 'AuthLoginController',
      controllerAs: 'vm',
      templateUrl: 'app/auth/login/authLogin.html'
    });
}

export default routerConfig;
