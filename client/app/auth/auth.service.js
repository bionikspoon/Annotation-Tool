class AuthService {
  constructor($http, AuthSession) {
    'ngInject';
    this.$http = $http;
    this.AuthSession = AuthSession;
  }

  login(credentials) {
    return this.$http
               .post('/login', credentials)
               .then(response => {
                 this.AuthSession.create(response.data.id, response.data.user.id, response.data.user.role);
                 return response.data.user;
               });
  }

  isAuthenticated() {
    return !!this.AuthSession.userId;
  }

  isAuthorized(authorizedRoles) {
    if(!angular.isArray(authorizedRoles)) {authorizedRoles = [authorizedRoles];}
    return (this.isAuthenticated() && authorizedRoles.indexOf(this.AuthSession.userRole) !== -1);
  }
}

export default AuthService;
