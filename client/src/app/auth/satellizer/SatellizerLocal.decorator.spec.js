(function() {
    'use strict';

    describe('SatellizerLocal.decorator.spec', function() {
        var SatellizerLocal;

        beforeEach(module('app.auth'));
        beforeEach(inject(function(_SatellizerLocal_) {
            SatellizerLocal = _SatellizerLocal_;
        }));

        describe('When logging in', function() {
            var $rootScope;
            beforeEach(inject(function(_$rootScope_) {
                $rootScope = _$rootScope_;
                spyOn($rootScope, '$broadcast');
            }));
            it('Should broadcast an auth login event', inject(function(AUTH_EVENT) {

            }));
        });

        describe('When verifying a token', function() {

        });

        describe('When refreshing a token', function() {

        });
    });

})();
