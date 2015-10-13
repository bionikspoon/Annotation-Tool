export default class UserController {
  constructor(AuthService, $scope, Session, SESSION_EVENTS, $log) {
    'ngInject';

    this.currentUser = {data: null};

    this.isAuthenticated = AuthService.isAuthenticated;
    this.isAuthorized = AuthService.isAuthorized;


    $scope.$on(SESSION_EVENTS.destroyed, () => this.setCurrentUser(null));
    $scope.$on(SESSION_EVENTS.created, () => this.setCurrentUser(Session));

    this.activate(Session);
  }

  activate(Session) {
    if(Session.exists()) {this.setCurrentUser(Session);}
  }

  setCurrentUser(user) {
    this.currentUser.data = user;
    return this.currentUser;
  }

}

