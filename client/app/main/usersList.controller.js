export default class UsersListController {
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
