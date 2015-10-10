(function() {
  'use strict';

  describe('controllers', function() {

    beforeEach(module('app'));

    it('should define more than 5 awesome things', inject(function($controller) {
      var main = $controller('MainController');

      expect(angular.isArray(main.awesomeThings)).toBeTruthy();
      expect(main.awesomeThings.length > 4).toBeTruthy();
    }));
  });
})();
