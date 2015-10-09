class AuthService {
  constructor($log, $http, $window, $q, Session) {
    'ngInject';
    this.$log = $log;
    this.$http = $http;
    this.$window = $window;
    this.$q = $q;
    this.Session = Session;
  }

  login(credentials) {
    return this.$http
               .post('api/auth/login/', credentials)
               .then(response => {
                 this.$log.debug('auth.service response:', response);

                 const base64 = response.data.token.split('.')[1];
                 const user = JSON.parse(this.$window.atob(base64));

                 this.Session.create(user);
                 return user;

               })
               .catch(error => {
                 this.$log.error('auth.service error:', error);
                 return this.$q.reject(error);
               });
  }

  isAuthenticated() {
    return !!this.Session.userId;
  }

  isAuthorized(authorizedRoles) {
    if(!angular.isArray(authorizedRoles)) {authorizedRoles = [authorizedRoles];}
    return (this.isAuthenticated() && authorizedRoles.indexOf(this.Session.userRole) !== -1);
  }
}

export default AuthService;
