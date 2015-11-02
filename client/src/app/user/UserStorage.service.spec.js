/* global localStorage */
(function() {
    'use strict';

    describe('userStorage.service.spec', function() {
        var UserStorage;
        var mockUser = getMockUser();
        var userKey = 'anno_user';

        beforeEach(module('app.user', 'mock.localStorage'));
        beforeEach(inject(function(_UserStorage_) {
            UserStorage = _UserStorage_;
            UserStorage.set(mockUser);
        }));

        describe('When setting a value', function() {

            it('should store the user value with a key', function() {
                expect(localStorage.setItem).toHaveBeenCalledWith(userKey, JSON.stringify(mockUser));
            });
        });

        describe('When getting a value', function() {

            it('should be using the configured key', function() {
                UserStorage.get();
                expect(localStorage.getItem).toHaveBeenCalledWith(userKey);
            });

            it('should deserialize to the original value', function() {
                var user = UserStorage.get();
                expect(user).toEqual(mockUser);
            });
        });

        describe('When removing a user', function() {

            it('should remove the key', function() {
                UserStorage.remove();
                expect(localStorage.removeItem).toHaveBeenCalledWith(userKey);

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
