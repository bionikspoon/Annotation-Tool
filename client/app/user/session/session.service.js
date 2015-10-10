export default class Session {
  constructor(USER_ROLES, SESSION_EVENTS, $window, $q, $rootScope) {
    'ngInject';
    this.USER_ROLES = USER_ROLES;
    this.SESSION_EVENTS = SESSION_EVENTS;
    this.$window = $window;
    this.$q = $q;

    _parseToken = angular.bind(this, _parseToken);
    _broadcast = angular.bind(null, _broadcast, $rootScope);
  }

  get token() {
    const _token = this.$window.localStorage.jwtToken;
    return _token === 'undefined' ? undefined : _token;
  }

  set token(value) {
    if(angular.isDefined(value)) {
      this.$window.localStorage.jwtToken = value;
    } else {
      this.deleteToken();
    }
  }

  deleteToken() {
    return this.$window.localStorage.removeItem('jwtToken');
  }


  _create(user) {
    const deferred = this.$q.defer();

    this.userId = user.user_id;
    this.email = user.email;
    this.username = user.username;
    this.exp = new Date(user.exp * 1000);
    this.role = this.USER_ROLES.admin;
    if(this.isExpired()) {
      deferred.reject(this.destroy());
    } else {
      deferred.resolve(this);
    }
    return deferred.promise;
  }

  create(token = false) {
    const deferred = this.$q.defer();
    this.token = token || this.token;
    if(angular.isDefined(this.token)) {

      this._create(_parseToken())
          .then(user => deferred.resolve(user))
          .catch(() => deferred.reject(this.SESSION_EVENTS.destroyed));

    } else {
      //this.destroy();
      deferred.reject(this.SESSION_EVENTS.destroyed);
    }
    return deferred.promise
                   .then(() => {
                     _broadcast(this.SESSION_EVENTS.created);
                     return this;
                   })
                   .catch(error => {
                     _broadcast(error);
                     return this.$q.reject(error);
                   });
  }

  destroy() {
    this.deleteToken();
    this.userId = null;
    this.email = null;
    this.username = null;
    this.exp = null;
    this.role = null;
    return this;
  }

  exists() {
    return angular.isDefined(this.token) && this.exp > new Date().getTime();
  }

  isExpired() {
    return this.exp < new Date().getTime();
  }

}

function _parseToken() {
  return JSON.parse(this.$window.atob(this.token.split('.')[1]));
}

function _broadcast($rootScope, SESSION_EVENTS, event) {
  $rootScope.$broadcast(SESSION_EVENTS[event]);
}
