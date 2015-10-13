/* global MockAuthService:false */
class MockAuthService {
  constructor($q) {
    'ngInject';
    this.$q = $q;

    this.login = jasmine.createSpy('login').and.callFake(this.fakeLogin);
    this.logout = jasmine.createSpy('logout');
    this.isAuthenticated = jasmine.createSpy('isAuthenticated');
    this.isAuthorized = jasmine.createSpy('isAuthorized');
  }

  fakeLogin(username) {
    const deferred = this.$q.defer();
    deferred.resolve({username: username});
    return deferred.promise;

  }

}


//angular.module('app.auth')
//       .service('AuthService', AuthService);
