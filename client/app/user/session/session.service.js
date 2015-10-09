class SessionService {
  constructor(USER_ROLES) {
    'ngInject';
    this.USER_ROLES = USER_ROLES;
  }


  create(user) {

    this.userId = user.user_id;
    this.email = user.email;
    this.username = user.username;
    this.exp = user.exp;
    this.role = this.USER_ROLES.admin;


  }

  destroy() {
    this.userId = null;
    this.email = null;
    this.username = null;
    this.exp = null;
    this.role = null;
  }
}

export default SessionService;
