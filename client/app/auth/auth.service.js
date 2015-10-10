export default class AuthService {
  constructor($log, $http, $q, AUTH_EVENTS, Session, $rootScope) {
    'ngInject';

    this.$log = $log;
    this.$http = $http;
    this.$q = $q;
    this.Session = Session;
    this.AUTH_EVENTS = AUTH_EVENTS;

    _broadcast = angular.bind(null, _broadcast, $rootScope);

    this.logout = angular.bind(this, this.logout);
    this.login = angular.bind(this, this.login);
    this.isAuthenticated = angular.bind(this, this.isAuthenticated);
    this.isAuthorized = angular.bind(this, this.isAuthorized);
  }

  login(credentials) {
    const deferred = this.$q.defer();
    this.$http
        .post('api/auth/login/', credentials)
        .then(response => deferred.resolve(this.Session.create(response.data.token)))
        .catch(error => deferred.reject(error));

    return deferred.promise
                   .then(() => {
                     _broadcast(this.AUTH_EVENTS.loginSuccess);
                     return this.Session;
                   })
                   .catch(error => {
                     _broadcast(this.AUTH_EVENTS.loginFailed);
                     return this.$q.reject(error);
                   });
  }


  logout() {
    _broadcast(this.AUTH_EVENTS.logoutSuccess);
    this.Session.destroy();
  }

  isAuthenticated() {
    return this.Session.exists();
  }

  isAuthorized(authorizedRoles) {
    if(!angular.isArray(authorizedRoles)) {authorizedRoles = [authorizedRoles];}
    return (this.isAuthenticated() && authorizedRoles.indexOf(this.Session.role) !== -1);
  }
}

function _broadcast($rootScope, event) {
  $rootScope.$broadcast(event);
}
