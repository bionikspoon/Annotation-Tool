(function() {
    'use strict';

    describe('controlsFormMeta.directive.spec', function() {
        beforeEach(module('app.controls'));

        var $compile;
        var $rootScope;
        var $scope;
        var mockMeta = {
            "mock_text": {
                "type":       "string",
                "required":   false,
                "read_only":  false,
                "label":      "Mock Text",
                "max_length": 128,
                "name":       "mock_text"
            }
        };

        beforeEach(inject(function(_$compile_, _$rootScope_) {
            $compile = _$compile_;
            $rootScope = _$rootScope_;
            $scope = $rootScope.$new();
            $scope.meta = mockMeta;
        }));

        describe('Compiled template', function() {
            var element;
            var formMetaCtrl;
            beforeEach(function() {
                var template = '<form app-form-meta=meta name=testForm></form>';
                element = $compile(template)($scope);
                formMetaCtrl = element.controller('appFormMeta');
            });
            it('should create a controller with form meta', function() {
                expect(formMetaCtrl.meta).toBe(mockMeta);
            });
            it('should have a form controller available as a promise', inject(function() {
                $rootScope.$apply();
                expect(formMetaCtrl.form.$name).toBe('testForm');
            }));
        });

    });

})();
