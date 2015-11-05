(function() {
    'use strict';

    describe('SatellizerStorage.decorator.spec', function() {
        var SatellizerStorage;
        var $rootScope;
        var AUTH_EVENT;
        var tokenName = 'anno_token';

        beforeEach(module('app.auth'));
        beforeEach(inject(function(_$rootScope_, _SatellizerStorage_, _AUTH_EVENT_) {
            $rootScope = _$rootScope_;
            SatellizerStorage = _SatellizerStorage_;
            AUTH_EVENT = _AUTH_EVENT_;
            spyOn($rootScope, '$broadcast');

        }));

        describe('When setting a token', function() {

            it('Should broadcast an auth event', function() {
                SatellizerStorage.set(tokenName, 'abc');
                expect($rootScope.$broadcast).toHaveBeenCalledWith(AUTH_EVENT.tokenSet);

            });

            it('Should only broadcast when key is the token', function() {
                SatellizerStorage.set('token', 'abc');
                expect($rootScope.$broadcast).not.toHaveBeenCalledWith(AUTH_EVENT.tokenSet);

            });
        });

        describe('When removing a token', function() {

            it('Should broadcast an auth event', function() {
                SatellizerStorage.remove(tokenName);
                expect($rootScope.$broadcast).toHaveBeenCalledWith(AUTH_EVENT.tokenRemove);
            });

            it('Should only broadcast when key is the token', function() {
                SatellizerStorage.remove('token');
                expect($rootScope.$broadcast).not.toHaveBeenCalledWith(AUTH_EVENT.tokenRemove);

            });
        });
    });

})();
