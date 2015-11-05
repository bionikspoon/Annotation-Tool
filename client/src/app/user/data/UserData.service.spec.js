(function() {
    'use strict';

    describe('UserData.service.spec', function() {
        var UserData;
        var $httpBackend;
        var mockUser = getMockUser();
        var mockError = getMockError();
        var profileEndpoint = '/api/auth/profile/';

        beforeEach(module('app.user'));
        beforeEach(inject(function(_$httpBackend_, _UserData_) {
            $httpBackend = _$httpBackend_;
            UserData = _UserData_;
        }));

        afterEach(function() {
            $httpBackend.verifyNoOutstandingExpectation();
            $httpBackend.verifyNoOutstandingRequest();
        });

        describe('When http request is successful', function() {
            beforeEach(function() {
                $httpBackend.whenGET(profileEndpoint)
                            .respond(mockUser);
            });

            it('Should call the api endpoint', function() {
                $httpBackend.expectGET(profileEndpoint);
                UserData.get();
                $httpBackend.flush();

            });
            it('Should fetch user profile', function() {
                var user = {};
                UserData
                    .get()
                    .then(function(response) {
                        user = response;
                    });
                $httpBackend.flush();

                expect(user.id).toEqual(mockUser.id);
                expect(user.email).toEqual(mockUser.email);
                expect(user.name).toEqual(mockUser.name);
                expect(user.username).toEqual(mockUser.username);

            });
        });
        describe('When http request fails', function() {
            beforeEach(function() {
                $httpBackend.whenGET(profileEndpoint)
                            .respond(400, mockError);
            });
            it('Should call the api endpoint', function() {
                $httpBackend.expectGET(profileEndpoint);
                UserData.get();
                $httpBackend.flush();

            });
            it('Should reject the promise', function() {
                var detail = {};
                UserData
                    .get()
                    .catch(function(error) {
                        detail = error.data;
                    });
                $httpBackend.flush();
                expect(detail).toEqual(mockError);
            });
        });

    });

    function getMockUser() {
        return Object.freeze({
            id:                  1,
            get_all_permissions: [],
            email:               'testUser@test.com',
            groups:              [],
            name:                'Test User',
            username:            'testUser'
        });
    }

    function getMockError() {
        return Object.freeze({
            detail: 'Authentication credentials were not provided.'
        });
    }

})();
