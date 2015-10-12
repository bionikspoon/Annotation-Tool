export default class AuthService {
  constructor($log, $http, $q, AUTH_EVENTS, Session, $rootScope, Toast, $state) {
    'ngInject';

    this.$log = $log;
    this.$http = $http;
    this.$q = $q;
    this.Session = Session;
    this.AUTH_EVENTS = AUTH_EVENTS;
    this.Toast = Toast;
    this.$state = $state;
    $rootScope.$on(AUTH_EVENTS.notAuthenticated, this.authenticationRequired.bind(this));
    $rootScope.$on(AUTH_EVENTS.notAuthorized, this.authorizationRequired.bind(this));
    _broadcast = angular.bind(null, _broadcast, $rootScope);
    return {
      logout: this.logout.bind(this),
      login: this.login.bind(this),
      isAuthenticated: this.isAuthenticated.bind(this),
      isAuthorized: this.isAuthorized.bind(this)
    };
  }

  authenticationRequired(event, response) {
    event.preventDefault();
    this.$state.go('auth.login');
    this.Toast.warning('Login Required', response.data.detail);
  }

  authorizationRequired(event, response) {
    event.preventDefault();
    this.$state.go('pubmed.list');
    this.Toast.warning('Insufficient Permissions', response.data.detail);
  }


  login(credentials) {
    const deferred = this.$q.defer();
    this.$http
        .post('api/auth/login/', credentials)
        .then(response => deferred.resolve(this.Session.create(response.data.token)))
        .catch(error => deferred.reject(error));

    return deferred.promise
                   .then(() => {
                     this.Toast.success('Signed In');
                     _broadcast(this.AUTH_EVENTS.loginSuccess);
                     return this.Session;
                   })
                   .catch(error => {
                     let message = '';
                     if(angular.isDefined(error.data)) {
                       angular.forEach(error.data, (field, key) => {
                         message += '<p><b>' + key + '</b>: ' + field[0] + '</p>';
                       });

                     }
                     this.Toast.error('Authentication Failed', message);
                     _broadcast(this.AUTH_EVENTS.loginFailed);
                     return this.$q.reject(error);
                   });
  }


  logout() {
    this.Toast.info('Signed Out');
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
