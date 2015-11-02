(function() {
    'use strict';

    describe('Session.factory.spec', function() {
        var Session;
        var UserStorage;
        var UserData;
        var $rootScope;
        var AUTH_EVENTS;
        var mockUser = getMockUser();

        beforeEach(module('app.user', 'mock.UserStorage', 'mock.UserData'));
        beforeEach(inject(function(_Session_, _UserStorage_, _UserData_, _$rootScope_, _AUTH_EVENTS_) {
            Session = _Session_;
            UserStorage = _UserStorage_;
            UserData = _UserData_;
            $rootScope = _$rootScope_;
            AUTH_EVENTS = _AUTH_EVENTS_;

            UserData.mockUser = mockUser;
        }));

        describe('When creating a session', function() {
            it('should delegate persistence to UserStorage', function() {
                Session.create(mockUser);
                expect(UserStorage.set).toHaveBeenCalledWith(mockUser);
            });

        });

        describe('When destroying a session', function() {
            beforeEach(function() {
                Session.create(mockUser);
            });
            it('should delegate persistence to UserStorage', function() {
                Session.destroy();

                expect(UserStorage.remove).toHaveBeenCalled();

            });
        });

        describe('When initializing a session', function() {
            describe('When UserData is resolved', function() {
                it('should call create with a user', function() {
                    spyOn(Session, 'create').and.callThrough();
                    Session.init();
                    $rootScope.$apply();

                    expect(Session.create).toHaveBeenCalledWith(mockUser);
                });
                it('should set user property', function() {
                    Session.init();
                    $rootScope.$apply();

                    expect(Session.user).toEqual(mockUser);
                });

            });
            describe('When UserData is rejected', function() {
                beforeEach(function() {
                    UserData.reject = true;
                });
                it('should destroy the session', function() {
                    spyOn(Session, 'destroy');
                    Session.init();
                    $rootScope.$apply();

                    expect(Session.destroy).toHaveBeenCalled();
                });
            });
        });

    });
    function getMockUser() {
        return {
            "id":          1,
            "permissions": [],
            "email":       "testUser@test.com",
            "groups":      [],
            "name":        "Test User",
            "username":    "testUser"
        };
    }

})();

//(function() {
//    'use strict';
//
//    // mockController
//    angular
//        .module('mock.controller', [])
//        .controller('mockController', mockController);
//
//    /** @ngInject **/
//    function mockController(Session) {
//        //var vm = this;
//        //vm.title = 'mockMockControllerController';
//        //
//        //activate();
//        //
//        //////////////////
//        //
//        //function activate() {
//        //
//        //}
//    }
//
//})();

