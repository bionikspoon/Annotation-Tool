(function() {
    'use strict';

    describe('$auth.decorator.spec', function() {
        var $auth;

        beforeEach(module('app.auth'));
        beforeEach(inject(function(_$auth_) {
            $auth = _$auth_;
        }));

        describe('When verifying a token', function() {
            var SatellizerLocal;
            beforeEach(inject(function(_SatellizerLocal_) {
                SatellizerLocal = _SatellizerLocal_;
                spyOn(SatellizerLocal, 'verify');
            }));

            it('Should delegate to local.verify', function() {
                var opts = {mockOptions: 'mockOptions'};
                $auth.verify(opts);

                expect(SatellizerLocal.verify).toHaveBeenCalledWith(opts);
            });

        });

        describe('When checking user can access permission', function() {
            var Session;
            var mockUser;

            beforeEach(inject(function(_Session_) {
                Session = _Session_;
                mockUser = getMockUser();
            }));

            afterEach(function() {
                Session.destroy();
            });

            it('Should check that user has permissions', function() {
                Session.create(mockUser);

                expect($auth.can('pubmed.add_pubmed')).toBeTruthy();
                expect($auth.can('pubmed.change_pubmed')).toBeTruthy();
                expect($auth.can('pubmed.delete_pubmed')).toBeFalsy();

            });

            it('Should deny permission for missing user', function() {
                expect($auth.can('pubmed.add_pubmed')).toBeFalsy();
                expect($auth.can('pubmed.delete_pubmed')).toBeFalsy();
            });
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
