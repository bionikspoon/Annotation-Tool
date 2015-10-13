export default function routerConfig($stateProvider) {
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
      template: '<pre><code>{{vm.users|json}}</code></pre>',
      controller: UsersListController,
      controllerAs: 'vm'

    });

}

class UsersListController {
  constructor(Restangular, $log, $q) {
    'ngInject';

    this.Restangular = Restangular;
    this.$log = $log;
    this.$q = $q;
    this.users = [];
    this.activate();
  }

  activate() {
    this.Restangular.all('users').getList()
        .then(users => {
          this.$log.debug('usersList.controller users:', users);
          this.users = users;
          return users;
        })
        .catch(error=> {
          this.$log.error('usersList.controller error:', error);
          this.$q.reject(error);
        });
  }
}
