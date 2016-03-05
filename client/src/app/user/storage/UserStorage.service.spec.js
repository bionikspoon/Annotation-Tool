/* global localStorage */
(function() {
    'use strict';

    describe('UserStorage.service.spec', function() {
        var UserStorage;
        var mockUser = getMockUser();
        var userKey = 'anno_user';

        beforeEach(module('mock.localStorage', 'app.user'));
        beforeEach(inject(function(_UserStorage_) {
            UserStorage = _UserStorage_;
            UserStorage.set(mockUser);
        }));

        describe('When setting a value', function() {

            it('Should store the user value with a key', function() {
                expect(localStorage.setItem).toHaveBeenCalledWith(userKey, JSON.stringify(mockUser));
            });
        });

        describe('When getting a value', function() {

            it('Should be using the configured key', function() {
                UserStorage.get();
                expect(localStorage.getItem).toHaveBeenCalledWith(userKey);
            });

            it('Should deserialize to the original value', function() {
                var user = UserStorage.get();
                expect(user).toEqual(mockUser);
            });
        });

        describe('When removing a user', function() {

            it('Should remove the key', function() {
                UserStorage.remove();
                expect(localStorage.removeItem).toHaveBeenCalledWith(userKey);

            });

        });

    });

    function getMockUser() {
        return Object.freeze({
            "id":          1,
            "permissions": [],
            "email":       "testUser@test.com",
            "groups":      [],
            "name":        "Test User",
            "username":    "testUser"
        });
    }

})();
