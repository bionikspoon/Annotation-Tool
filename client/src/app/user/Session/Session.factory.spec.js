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
            it('Should delegate persistence to UserStorage', function() {
                Session.create(mockUser);
                expect(UserStorage.set).toHaveBeenCalledWith(mockUser);
            });

        });

        describe('When destroying a session', function() {
            beforeEach(function() {
                Session.create(mockUser);
            });
            it('Should delegate persistence to UserStorage', function() {
                Session.destroy();

                expect(UserStorage.remove).toHaveBeenCalled();

            });
        });

        describe('When initializing a session', function() {
            describe('When UserData is resolved', function() {
                it('Should call create with a user', function() {
                    spyOn(Session, 'create').and.callThrough();
                    Session.init();
                    $rootScope.$apply();

                    expect(Session.create).toHaveBeenCalledWith(mockUser);
                });
                it('Should set user property', function() {
                    Session.init();
                    $rootScope.$apply();

                    expect(Session.user).toEqual(mockUser);
                });

            });
            describe('When UserData is rejected', function() {
                beforeEach(function() {
                    UserData.reject = true;
                });
                it('Should destroy the session', function() {
                    spyOn(Session, 'destroy');
                    Session.init();
                    $rootScope.$apply();

                    expect(Session.destroy).toHaveBeenCalled();
                });
            });
        });

        it('Should check that user has permissions', function() {
            Session.create(mockUser);

            expect(Session.can('pubmed.add_pubmed')).toBeTruthy();
            expect(Session.can('pubmed.change_pubmed')).toBeTruthy();
            expect(Session.can('pubmed.delete_pubmed')).toBeFalsy();

        });

        it('Should deny permission for missing user', function() {

            expect(Session.can('pubmed.add_pubmed')).toBeFalsy();
            expect(Session.can('pubmed.delete_pubmed')).toBeFalsy();
        });

    });
    function getMockUser() {
        return Object.freeze({
            id:          1,
            permissions: [
                'pubmed.add_pubmed',
                'pubmed.change_pubmed'
            ],
            email:       'testUser@test.com',
            groups:      [],
            name:        'Test User',
            username:    'testUser'
        });
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

