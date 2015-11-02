(function() {
    'use strict';

    describe('Satellizer.decorator.spec', function() {

        beforeEach(module('app.auth'));

        describe('storage decorator', function() {
            var SatellizerStorage;
            var $rootScope;
            var AUTH_EVENTS;
            var tokenName = 'anno_token';

            beforeEach(inject(function(_$rootScope_, _SatellizerStorage_, _AUTH_EVENTS_) {
                $rootScope = _$rootScope_;
                SatellizerStorage = _SatellizerStorage_;
                AUTH_EVENTS = _AUTH_EVENTS_;
                spyOn($rootScope, '$broadcast');

            }));

            describe('When setting a token', function() {

                it('Should broadcast an auth event', function() {
                    SatellizerStorage.set(tokenName, 'abc');
                    expect($rootScope.$broadcast).toHaveBeenCalledWith(AUTH_EVENTS.tokenSet);

                });

                it('Should only broadcast when key is the token', function() {
                    SatellizerStorage.set('token', 'abc');
                    expect($rootScope.$broadcast).not.toHaveBeenCalledWith(AUTH_EVENTS.tokenSet);

                });
            });

            describe('When removing a token', function() {

                it('Should broadcast an auth event', function() {
                    SatellizerStorage.remove(tokenName);
                    expect($rootScope.$broadcast).toHaveBeenCalledWith(AUTH_EVENTS.tokenRemove);
                });

                it('Should only broadcast when key is the token', function() {
                    SatellizerStorage.remove('token');
                    expect($rootScope.$broadcast).not.toHaveBeenCalledWith(AUTH_EVENTS.tokenRemove);

                });
            });
        });

        describe('local decorator', function() {
            var SatellizerLocal;
            beforeEach(inject(function(_SatellizerLocal_) {
                SatellizerLocal = _SatellizerLocal_;
            }));

            describe('When logging in', function() {

            });

            describe('When verifying a token', function() {

            });

            describe('When refreshing a token', function() {

            });
        });

        describe('$auth decorator', function() {
            var $auth;
            beforeEach(inject(function(_$auth_) {
                $auth = _$auth_;
            }));

            describe('When verifying a token', function () {

            });

        });

    });

})();
