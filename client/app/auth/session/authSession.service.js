class AuthSessionService {
  constructor() {
    'ngInject';
  }

  create(sessionId, userId, userRole) {
    this.sessionId = sessionId;
    this.userId = userId;
    this.userRole = userRole;
  }

  destroy() {
    this.id = null;
    this.userId = null;
    this.userRole = null;
  }
}

export default AuthSessionService;
