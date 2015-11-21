(function() {
    'use strict';

    describe('authLogin.controller.spec', function() {
        var $rootScope;
        var $scope;
        var vm;
        var $auth;

        beforeEach(module('app.auth', 'mock.$auth', 'mock.AuthLoginData'));
        beforeEach(inject(function(_$rootScope_, _$controller_, _$auth_) {
            var $controller = _$controller_;
            $rootScope = _$rootScope_;
            $scope = $rootScope.$new();
            vm = $controller('authLoginController', {$scope: $scope});
            $auth = _$auth_;
        }));
        describe('Login', function() {
            var credentials;
            var loginResponse;
            var $state;

            beforeEach(inject(function(_$state_) {
                $state = _$state_;
                spyOn($state, 'go');
                credentials = {
                    username: 'admin',
                    password: 'secret'
                };
                $auth.loginExpect(credentials);

            }));
            describe('When login is successful', function() {
                beforeEach(function() {
                    loginResponse = $auth.loginResolve();
                });

                it('Should be resolved', function() {
                    var response = {};
                    vm.login(credentials)
                      .then(function(_response) {
                          response = _response;
                      });
                    $rootScope.$apply();
                    expect(response).toEqual(loginResponse);
                    expect($state.go).toHaveBeenCalledWith('pubmed.list', {});
                });
            });

            describe('When login fails', function() {
                beforeEach(function() {
                    credentials.password = 'password';
                    loginResponse = $auth.loginReject();
                });

                it('Should be rejected', function() {
                    var error = {};

                    vm.login(credentials)
                      .then(angular.identity)
                      .catch(function(_error) {
                          error = _error;
                      });
                    $rootScope.$apply();
                    expect(error).toEqual(loginResponse);

                });
            });
        });

    });

})();
