class MockAuthService {
  constructor() {
    'ngInject';

    this.login = jasmine.createSpy('login');
    this.logout = jasmine.createSpy('logout');
    this.isAuthenticated = jasmine.createSpy('isAuthenticated');
    this.isAuthorized = jasmine.createSpy('isAuthorized');
  }

}




//angular.module('app.auth')
//       .service('AuthService', AuthService);
