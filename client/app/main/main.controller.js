class MainController {
  constructor($log, AUTH_ROLES, AuthService) {
    'ngInject';
    this.$log = $log;
    this.currentUser = null;
    this.authRoles = AUTH_ROLES;
    this.isAuthorized = AuthService.isAuthorized;
  }

  setCurrentUser(user) {
    this.$log.debug('Setting current user.  main.controller user:', user);
    this.currentUser = user;
  }

}

export default MainController;
