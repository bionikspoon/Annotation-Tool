(function() {
    'use strict';

    describe('Session.factory.spec', function() {
        beforeEach(module('app.user'));
        var Session;
        beforeEach(inject(function(_Session_) {
            Session = _Session_;
        }));

        describe('When creating a session', function() {
            it('should save user to local storage', function() {

            });

        });

        describe('When destroying a session', function() {

        });

        describe('When initializing a session', function() {
            describe('When http request is successful', function() {
                it('Should call create with a user', function() {

                });
            });
            describe('When http request fails', function() {
                it('should destroy the session', function() {});
            });
        });


    });

})();
