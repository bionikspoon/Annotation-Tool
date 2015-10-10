const _USER_ROLES = new WeakMap();
const _SESSION_EVENTS = new WeakMap();
const _$window = new WeakMap();
const _$q = new WeakMap();
const _$rootScope = new WeakMap();
export default class Session {
  constructor(USER_ROLES, SESSION_EVENTS, $window, $q, $rootScope) {
    'ngInject';
    _USER_ROLES.set(this, USER_ROLES);
    _SESSION_EVENTS.set(this, SESSION_EVENTS);
    _$window.set(this, $window);
    _$q.set(this, $q);
    _$rootScope.set(this, $rootScope);
  }

  get token() {
    const _token = _$window.get(this).localStorage.jwtToken;
    return _token === 'undefined' ? undefined : _token;
  }

  set token(value) {
    _$window.get(this).localStorage.jwtToken = value;
  }

  deleteToken() {
    return _$window.get(this).localStorage.removeItem('jwtToken');
  }


  _create(user) {
    const deferred = _$q.get(this).defer();

    this.userId = user.user_id;
    this.email = user.email;
    this.username = user.username;
    this.exp = new Date(user.exp * 1000);
    this.role = _USER_ROLES.get(this).admin;
    if(this.isExpired()) {
      deferred.reject(this.destroy());
    } else {
      deferred.resolve(this);
    }
    return deferred.promise;
  }

  create(token = false) {
    const deferred = _$q.get(this).defer();
    this.token = token || this.token;
    if(angular.isDefined(this.token)) {

      this._create(_parseToken.bind(this)())
          .then(user => deferred.resolve(user))
          .catch(() => deferred.reject(_SESSION_EVENTS.get(this).destroyed));

    } else {
      //this.destroy();
      deferred.reject(_SESSION_EVENTS.get(this).destroyed);
    }
    return deferred.promise
                   .then(() => {
                     _$rootScope.get(this).$broadcast(_SESSION_EVENTS.get(this).created);
                     return this;
                   })
                   .catch(error => {
                     _$rootScope.get(this).$broadcast(error);
                     return _$q.get(this).reject(error);
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
    return this.exp > new Date().getTime();
  }

  isExpired() {
    return this.exp < new Date().getTime();
  }

}

function _parseToken() {
  return JSON.parse(_$window.get(this).atob(this.token.split('.')[1]));


}

