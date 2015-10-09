export default class UserController {
  constructor($log, USER_ROLES, AuthService) {
    'ngInject';

    this.$log = $log;
    this.authRoles = USER_ROLES;
    this.currentUser = null;

    this.isAuthorized = AuthService.isAuthorized;
  }

  setCurrentUser(user) {
    this.$log.debug('Setting current user.  user.controller user:', user);
    this.currentUser = user;
  }
}

