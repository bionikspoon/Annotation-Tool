/* global MockAuthService:false */
(() => {
  describe('AuthLoginDirective', () => {
    beforeEach(module('app.auth'));
    beforeEach(module($provide => { $provide.service('AuthService', MockAuthService);}));

    it('should log in the user', inject(($controller, AuthService) => {
      let vm = $controller('AuthLoginController');
      //console.debug('authLogin.controller.spec angular.mock.dump(vm):', angular.mock.dump(vm));
      expect(AuthService.login.calls.count()).toBe(0);
      vm.login('test_user')
        .then(result => {
          expect(result.username).toBe('test_user');
        });


    }));
  });

})();
