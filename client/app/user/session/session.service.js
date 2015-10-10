const _USER_ROLES = new WeakMap();
const _$window = new WeakMap();

export default class Session {
  constructor(USER_ROLES, $window, $log) {
    'ngInject';
    _USER_ROLES.set(this, USER_ROLES);
    _$window.set(this, $window);
    this.$log = $log;
  }

  get token() {
    return _$window.get(this).localStorage.jwtToken;
  }

  set token(value) {
    _$window.get(this).localStorage.jwtToken = value;
  }

  deleteToken() {
    return _$window.get(this).localStorage.removeItem('jwtToken');
  }


  _create(user) {

    this.userId = user.user_id;
    this.email = user.email;
    this.username = user.username;
    this.exp = new Date(user.exp * 1000);
    this.role = _USER_ROLES.get(this).admin;
    return this;
  }

  create(token = false) {
    this.token = token || this.token;
    const user = _parseToken.bind(this)();

    return this._create(user);
  }

  destroy() {
    this.deleteToken();
    this.userId = null;
    this.email = null;
    this.username = null;
    this.exp = null;
    this.role = null;
    return true;
  }

}

function _parseToken() {
  const base64 = this.token.split('.')[1];
  return JSON.parse(_$window.get(this).atob(base64));
}
