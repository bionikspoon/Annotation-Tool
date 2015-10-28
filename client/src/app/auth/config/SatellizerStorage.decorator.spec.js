(function() {
    'use strict';

    describe('SatellizerStorage.decorator.spec', function() {
        beforeEach(module('app.auth'));
        var $rootScope;
        var SatellizerStorage;
        var AUTH_EVENTS;
        var tokenName = 'anno_token';

        beforeEach(inject(function(_$rootScope_, _SatellizerStorage_, _AUTH_EVENTS_) {
            $rootScope = _$rootScope_;
            SatellizerStorage = _SatellizerStorage_;
            AUTH_EVENTS = _AUTH_EVENTS_;
            spyOn($rootScope, '$broadcast');
        }));
        describe('When setting a token', function() {
            it('should broadcast an auth event', function() {
                SatellizerStorage.set(tokenName, 'abc');
                expect($rootScope.$broadcast).toHaveBeenCalledWith(AUTH_EVENTS.tokenSet);

            });
            it('should only broadcast when key is the token', function() {
                SatellizerStorage.set('token', 'abc');
                expect($rootScope.$broadcast).not.toHaveBeenCalledWith(AUTH_EVENTS.tokenSet);

            });
        });
        describe('When removing a token', function() {
            it('should broadcast an auth event', function() {
                SatellizerStorage.remove(tokenName);
                expect($rootScope.$broadcast).toHaveBeenCalledWith(AUTH_EVENTS.tokenRemove);
            });
            it('should only broadcast when key is the token', function() {
                SatellizerStorage.remove('token');
                expect($rootScope.$broadcast).not.toHaveBeenCalledWith(AUTH_EVENTS.tokenRemove);

            });
        });
    });

})();
