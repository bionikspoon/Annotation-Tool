(function() {
    'use strict';

    describe('controllers', function() {

        beforeEach(module('app.main'));

        it('should define more than 5 awesome things!', inject(function($controller) {
            var vm = $controller('MainController');

            expect(angular.isDefined(vm.awesomeThings)).toBeFalsy();
        }));
    });
})();
