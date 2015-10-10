export default class AuthService {
  constructor($log, $http, $q, AUTH_EVENTS, Session, $rootScope) {
    'ngInject';
    this.$log = $log;
    this.$http = $http;
    this.$q = $q;
    this.Session = Session;
    this.AUTH_EVENTS = AUTH_EVENTS;
    $log.debug('auth.service this.Session:', this.Session);
    _broadcast = angular.bind(null, _broadcast, $rootScope);
  }

  login(credentials) {
    const deferred = this.$q.defer();
    this.$http
        .post('api/auth/login/', credentials)
        .then(response => deferred.resolve(this.Session.create(response.data.token)))
        .catch(error => deferred.reject(error));

    return deferred.promise
                   .then(() => {
                     this.$log.debug('Login Success auth.service this.Session:', this.Session);
                     _broadcast(this.AUTH_EVENTS.loginSuccess);
                     return this.Session;
                   })
                   .catch(error => {
                     this.$log.debug('Login Failed auth.service error:', error);
                     _broadcast(this.AUTH_EVENTS.loginFailed);
                     return this.$q.reject(error);
                   });
  }


  logout() {
    this.Session.destroy();
  }

  isAuthenticated() {
    //this.$log.debug('auth.service this.Session.exp, new Date().getTime():', this.Session.exp, new Date().getTime());
    this.$log.debug('auth.service this.Session:', this.Session);
    this.$log.debug('auth.service this:', this);
    return this.Session.exists();
  }

  isAuthorized(authorizedRoles) {
    if(!angular.isArray(authorizedRoles)) {authorizedRoles = [authorizedRoles];}
    return (this.isAuthenticated() && authorizedRoles.indexOf(this.Session.userRole) !== -1);
  }
}

function _broadcast($rootScope, event) {
  $rootScope.$broadcast(event);
}
