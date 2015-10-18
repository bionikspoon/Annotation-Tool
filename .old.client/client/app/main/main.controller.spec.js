(() => {
  'use strict';

  describe('controllers', () => {

    beforeEach(module('app.main'));

    it('it should be defined', inject($controller => {
      let main = $controller('MainController');

      expect(angular.isDefined(main)).toBeTruthy();
    }));
  });
})();
