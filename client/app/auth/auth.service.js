export default class AuthService {
  constructor($log, $http, $q, Session, $rootScope) {
    'ngInject';
    this.$log = $log;
    this.$http = $http;
    this.$q = $q;
    this.Session = Session;
    angular.bind(this, _broadcast, $rootScope);
    _broadcast = angular.bind(null, _broadcast, $rootScope);
  }

  login(credentials) {
    return this.$http
               .post('api/auth/login/', credentials)
               .then(response => {
                 return this.Session.create(response.data.token);
               })
               .catch(error => {
                 this.$log.error('auth.service error:', error);
                 return this.$q.reject(error);
               });
  }

  loginFromStorage() {
    return this.$q.resolve(this.Session.create())
               .then(result => {
                 if(!!result) {
                   return result;
                 } else {
                   this.$q.reject(result);
                 }
               });

  }

  logout() {
    this.Session.destroy();
  }

  isAuthenticated() {
    return this.Session.exp > new Date().getTime();
  }

  isAuthorized(authorizedRoles) {
    if(!angular.isArray(authorizedRoles)) {authorizedRoles = [authorizedRoles];}
    return (this.isAuthenticated() && authorizedRoles.indexOf(this.Session.userRole) !== -1);
  }
}

function _broadcast(user, $rootScope) {
  console.log(this);
  console.log(user);
  console.log($rootScope);
}
