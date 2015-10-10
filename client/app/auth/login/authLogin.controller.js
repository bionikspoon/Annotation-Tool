class AuthLoginController {
  constructor($rootScope, $scope, $q, $log, $state, AUTH_EVENTS, AuthService) {
    'ngInject';

    this.$rootScope = $rootScope;
    this.user = $scope.user;
    this.$log = $log;
    this.$q = $q;
    this.$state = $state;
    this.AUTH_EVENTS = AUTH_EVENTS;
    this.AuthService = AuthService;
  }


  login(credentials) {
    this.AuthService.login(credentials)
        .then(user => {
          this.$log.debug('authLogin.controller user:', user);
          //this.user.setCurrentUser(user);
          this.$state.go('pubmed.list');
        })
        .catch(error => {
          this.$log.error('authLogin.controller error:', error);
          this.$q.reject(error);
        });
  }


}

export default AuthLoginController;
