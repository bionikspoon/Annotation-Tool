class AuthLoginController {
  constructor($rootScope, AUTH_EVENTS, AuthService) {
    'ngInject';

    this.$rootScope = $rootScope;
    this.AUTH_EVENTS = AUTH_EVENTS;
    this.AuthService = AuthService;
  }


  login(credentials) {
    this.AuthService.login(credentials)
               .then(user => {
                 this.$rootScope.$broadcast(this.AUTH_EVENTS.loginSuccess);
                 this.setCurrentUser(user);
               })
               .catch(this.$rootScope.$broadcast(this.AUTH_EVENTS.loginFailed));
  }


}

export default AuthLoginController;
