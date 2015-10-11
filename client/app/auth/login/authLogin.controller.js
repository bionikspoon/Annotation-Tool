export default class AuthLoginController {
  constructor($q, $state, AuthService) {
    'ngInject';

    this.AuthService = AuthService;
    this.login = angular.bind(this, this.login, $q, $state);
  }


  login($q, $state, credentials) {
    this.AuthService.login(credentials)
        .then(user => {
          $state.go('pubmed.list');
          return user;
        })
        .catch(error => {
          $q.reject(error);
        });
  }
}
