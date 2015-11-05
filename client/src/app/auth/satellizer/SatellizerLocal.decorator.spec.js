/* global KJUR */
(function() {
    'use strict';

    describe('SatellizerLocal.decorator.spec', function() {
        var SatellizerLocal;
        var AUTH_EVENT;
        var $httpBackend;
        var $rootScope;
        var Session;
        var mockToken;
        var mockPayload;
        var mockCredentials;
        var mockUser;

        var loginEndpoint = '/api/auth/login/';
        var verifyEndpoint = '/api/auth/verify/';
        var profileEndpoint = '/api/auth/profile/';
        var refreshEndpoint = '/api/auth/refresh/';

        beforeEach(module('app.auth'));
        beforeEach(inject(function(_SatellizerLocal_, _AUTH_EVENT_, _$httpBackend_, _$rootScope_) {
            SatellizerLocal = _SatellizerLocal_;
            AUTH_EVENT = _AUTH_EVENT_;
            $httpBackend = _$httpBackend_;
            $rootScope = _$rootScope_;
            mockPayload = getMockPayload();
            mockToken = getMockToken(mockPayload);
            mockCredentials = getMockCredentials();
            mockUser = getMockUser();

        }));

        beforeEach(inject(function(_Session_) {
            $httpBackend.whenGET(profileEndpoint)
                        .respond(mockUser);

            Session = _Session_;
            spyOn(Session, 'init');
        }));

        afterEach(function() {
            $httpBackend.verifyNoOutstandingExpectation();
            $httpBackend.verifyNoOutstandingRequest();
        });

        describe('When logging in', function() {

            beforeEach(function() {

                $httpBackend.expectPOST(loginEndpoint, mockCredentials)
                            .respond(mockToken);

            });

            it('Should broadcast an auth login event', function() {
                spyOn($rootScope, '$broadcast').and.callThrough();

                SatellizerLocal.login(mockCredentials);
                expect($rootScope.$broadcast).not.toHaveBeenCalled();
                $httpBackend.flush();

                expect($rootScope.$broadcast).toHaveBeenCalledWith(AUTH_EVENT.login);
            });

            it('Should be authenticated', inject(function($auth) {

                SatellizerLocal.login(mockCredentials);
                $httpBackend.flush();
                expect($auth.isAuthenticated()).toBeTruthy();
            }));

            it('Should refresh on expiration', inject(function($timeout, SatellizerShared) {
                SatellizerLocal.login(mockCredentials);
                $httpBackend.flush();

                var expectHeaders = {
                    Accept:         'application/json, text/plain, */*',
                    'Content-Type': 'application/json;charset=utf-8',
                    Authorization:  'Bearer ' + mockToken.token
                };

                $httpBackend.expectPOST(refreshEndpoint, mockToken, expectHeaders)
                            .respond(function() {
                                mockToken = getMockToken(getMockPayload());
                                return mockToken;
                            });
                $timeout.flush();
                $httpBackend.flush();
                expect(SatellizerShared.getToken()).toBe(mockToken.token);
            }));
        });

        describe('When verifying a token', function() {
            beforeEach(inject(function(SatellizerShared) {
                var token = {
                    data: mockToken
                };
                SatellizerShared.setToken(token);

                $httpBackend.expectPOST(verifyEndpoint, mockToken)
                            .respond(200, mockToken);
            }));

            it('Should broadcast an auth verify event', function() {
                spyOn($rootScope, '$broadcast').and.callThrough();

                SatellizerLocal.verify();
                expect($rootScope.$broadcast).not.toHaveBeenCalled();

                $httpBackend.flush();
                expect($rootScope.$broadcast).toHaveBeenCalledWith(AUTH_EVENT.verify);

            });

            it('Should be authenticated', inject(function($auth) {

                SatellizerLocal.verify();
                $httpBackend.flush();

                expect($auth.isAuthenticated()).toBeTruthy();
            }));

        });

        describe('When refreshing a token', function() {
            beforeEach(inject(function(SatellizerShared) {
                var token = {
                    data: mockToken
                };
                SatellizerShared.setToken(token);

                $httpBackend.expectPOST(refreshEndpoint, mockToken)
                            .respond(200, mockToken);
            }));

            it('Should broadcast a refresh token', inject(function($timeout) {
                spyOn($rootScope, '$broadcast').and.callThrough();

                SatellizerLocal.refresh(1005);
                expect($rootScope.$broadcast).not.toHaveBeenCalled();

                $timeout.flush();
                $rootScope.$broadcast.calls.reset();
                $httpBackend.flush();
                expect($rootScope.$broadcast).toHaveBeenCalledWith(AUTH_EVENT.refresh);

            }));

            it('Should refresh on expiration', inject(function($timeout, SatellizerShared) {
                SatellizerLocal.refresh(1005);
                $timeout.flush();
                $httpBackend.flush();

                var expectHeaders = {
                    Accept:         'application/json, text/plain, */*',
                    'Content-Type': 'application/json;charset=utf-8',
                    Authorization:  'Bearer ' + mockToken.token
                };

                $httpBackend.expectPOST(refreshEndpoint, mockToken, expectHeaders)
                            .respond(function() {
                                mockToken = getMockToken(getMockPayload());
                                return mockToken;
                            });
                $timeout.flush();
                $httpBackend.flush();
                expect(SatellizerShared.getToken()).toBe(mockToken.token);
            }));

        });
    });

    function getMockToken(mockPayload) {
        var header = JSON.stringify({
            alg: 'HS256',
            typ: 'JWT'
        });
        var payload = JSON.stringify(mockPayload);
        var password = 'secret';
        return Object.freeze({token: KJUR.jws.JWS.sign('HS256', header, payload, password)});
    }

    function getMockPayload() {
        return Object.freeze({
            exp:      KJUR.jws.IntDate.get('now + 1hour'),
            orig_iat: KJUR.jws.IntDate.get('now'),
            user_id:  1,
            email:    "testUser@test.com",
            username: "testUser"
        });
    }

    function getMockCredentials() {
        return Object.freeze({
            username: 'testUser',
            password: 'secret'
        });
    }

    function getMockUser() {
        return Object.freeze({
            "id":                  1,
            "get_all_permissions": [],
            "email":               "testUser@test.com",
            "groups":              [],
            "name":                "Test User",
            "username":            "testUser"
        });
    }
})();
