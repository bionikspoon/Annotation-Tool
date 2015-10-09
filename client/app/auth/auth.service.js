class AuthService {
  constructor($log, $http, $window, $q, AuthSession) {
    'ngInject';
    this.$log = $log;
    this.$http = $http;
    this.$window = $window;
    this.$q = $q;
    this.AuthSession = AuthSession;
  }

  login(credentials) {
    return this.$http
               .post('api/auth/login/', credentials)
               .then(response => {
                 this.$log.debug('auth.service response:', response);

                 const base64 = response.data.token.split('.')[1];
                 const user = JSON.parse(this.$window.atob(base64));

                 this.AuthSession.create(user);
                 return user;

               })
               .catch(error => {
                 this.$log.error('auth.service error:', error);
                 return this.$q.reject(error);
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
