(() => {
  'use strict';

  describe('AuthLogoutDirective', () => {
    let element;

    beforeEach(module('app.auth'));

    beforeEach(module($provide => {$provide.service('AuthService', MockAuthService);}))

    beforeEach(inject(($compile, $rootScope) => {
      element = $compile('<button app-auth-logout>Button</button>')($rootScope);
    }));

    it('should not replace content', inject($rootScope => {
      $rootScope.$digest();

      expect(element.html()).toBe('Button');
    }));

    it('should call AuthService logout on click', inject(($rootScope, AuthService) => {
      $rootScope.$digest();
      expect(AuthService.logout.calls.count()).toBe(0);
      expect($rootScope.clicked).toBeFalsy();

      element.triggerHandler('click');

      expect(AuthService.logout.calls.count()).toBe(1);
    }));


  });


})();
