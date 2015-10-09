class AuthSessionService {
  constructor(AUTH_ROLES) {
    'ngInject';
    this.AUTH_ROLES = AUTH_ROLES;
  }


  create(user) {

    this.userId = user.user_id;
    this.email = user.email;
    this.username = user.username;
    this.exp = user.exp;
    this.role = this.AUTH_ROLES.admin;


  }

  destroy() {
    this.userId = null;
    this.email = null;
    this.username = null;
    this.exp = null;
    this.role = null;
  }
}

export default AuthSessionService;
