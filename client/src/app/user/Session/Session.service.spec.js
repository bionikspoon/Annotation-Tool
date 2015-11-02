(function() {
    'use strict';

    describe('Session.factory.spec', function() {
        beforeEach(module('app.user'));
        var Session;
        beforeEach(inject(function(_Session_) {
            Session = _Session_;
        }));
    });

})();
