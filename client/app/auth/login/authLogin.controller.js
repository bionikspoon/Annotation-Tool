class AuthLoginController {
  constructor($rootScope, $scope, $q, $log, AUTH_EVENTS, AuthService) {
    'ngInject';

    this.$rootScope = $rootScope;
    this.$scope = $scope;
    this.$log = $log;
    this.$q = $q;
    this.AUTH_EVENTS = AUTH_EVENTS;
    this.AuthService = AuthService;
  }


  login(credentials) {
    this.AuthService.login(credentials)
        .then(user => {
          this.$log.debug('authLogin.controller user:', user);
          this.$rootScope.$broadcast(this.AUTH_EVENTS.loginSuccess);
          this.$scope.main.setCurrentUser(user);
        })
        .catch(error => {
          this.$log.error('authLogin.controller error:', error);
          this.$rootScope.$broadcast(this.AUTH_EVENTS.loginFailed);
          this.$q.reject(error);
        });
  }


}

export default AuthLoginController;
