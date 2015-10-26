(function() {
    'use strict';

    describe('controlsFormMeta.directive.spec', function() {
        beforeEach(module('app.controls'));

        var $compile;
        var $rootScope;

        beforeEach(inject(function(_$compile_, _$rootScope_) {
            $compile = _$compile_;
            $rootScope = _$rootScope_;
            $rootScope.meta = {};
        }));

        it('does stuff', function() {
            //var element = $compile('<form app-form-meta=meta></form>')($rootScope);
            //$rootScope.$digest();
        });

    });

})();
