function routerConfig($stateProvider) {
  'ngInject';
  $stateProvider
    .state('main', {
      url: '/',
      templateUrl: 'app/main/main.html',
      controller: 'MainController',
      controllerAs: 'main',
      abstract: true
    })

    .state('users', {
      url: 'users/',
      template: '<ui-view/>',
      abstract: true,
      parent: 'main'

    })
    .state('users.list', {
      url: '',
      templateUrl: 'app/main/usersList.html',
      controller: 'UsersListController',
      controllerAs: 'vm'

    })

}

export default routerConfig;
