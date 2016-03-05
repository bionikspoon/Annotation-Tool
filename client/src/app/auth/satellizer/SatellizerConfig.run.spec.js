(function() {
    'use strict';

    describe('SatellizerConfig.run.spec', function() {
        var SatellizerConfig;

        beforeEach(module('app.auth'));
        beforeEach(inject(function(_SatellizerConfig_) {
            SatellizerConfig = _SatellizerConfig_;
        }));

        it('Should define verifyUrl', function() {
            expect(SatellizerConfig.verifyUrl).toBe('/auth/verify/');
        });

        it('Should define refreshUrl', function() {
            expect(SatellizerConfig.refreshUrl).toBe('/auth/refresh/');
        });

    });

})();
