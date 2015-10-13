export default class AuthLoginController {
  constructor($q, $state, AuthService, Toast) {
    'ngInject';

    this.AuthService = AuthService;
    this.Toast = Toast;
    this.$q = $q;
    this.$state = $state;
  }


  login(credentials) {
    this.AuthService.login(credentials)
        .then(user => {
          this.$state.go('pubmed.list');
          return user;
        })
        .catch(error => {
          return this.$q.reject(error);
        });
  }
}
