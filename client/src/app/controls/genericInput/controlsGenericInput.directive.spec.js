(function() {
    'use strict';

    describe('controlsGenericInput.directive.spec', function() {
        var $compile;
        var $rootScope;
        var $scope;
        var element;
        var mockMeta = getMockMeta();

        beforeEach(module('app.controls'));

        beforeEach(inject(function(_$compile_, _$rootScope_) {
            $compile = _$compile_;
            $rootScope = _$rootScope_;
            $scope = $rootScope.$new();
            $scope.meta = mockMeta;
        }));

        describe('Text input', function() {

            beforeEach(function() {
                var template = '<form app-form-meta=meta><app-generic-input ng-model=data.mock_text></app-generic-input></form>';
                element = $compile(template)($scope);
                $scope.$digest();
            });

            it('Should render text input', function() {
                var input = element.find('input');
                expect(input.length).toBe(1);
                expect(input.attr('type')).toBe('text');
            });

            it('Should have the attributes described in meta', function() {
                var input = element.find('input');
                expect(input.attr('name')).toBe(mockMeta.mock_text.name);
                expect(input.attr('ng-maxlength')).toBe(mockMeta.mock_text.max_length.toString());
            });

            it('Should have a label populated from meta', function() {
                var label = element.find('label');
                expect(label.length).toBe(1);
                expect(label.html()).toBe(mockMeta.mock_text.label);
            });

            it('Should create a label from attr', function() {
                var label = element.find('label');
                var input = element.find('input');
                expect(label.attr('for')).toBe(input.attr('id'));

            });
        });

        describe('Number input', function() {

            beforeEach(function() {
                var template = '<form app-form-meta=meta><app-generic-input ng-model=data.mock_number></app-generic-input></form>';
                element = $compile(template)($scope);
                $scope.$digest();
            });

            it('Should render number input', function() {
                var input = element.find('input');
                expect(input.attr('type')).toBe('number');
            });

        });

        describe('Textarea', function() {

            beforeEach(function() {
                var template = '<form app-form-meta=meta><app-generic-input ng-model=data.mock_textarea></app-generic-input></form>';
                element = $compile(template)($scope);
                $scope.$digest();
            });

            it('Should render a textarea', function() {
                var textarea = element.find('textarea');
                expect(textarea.length).toBe(1);
            });

            it('Should not render any inputs', function() {
                var input = element.find('input');
                expect(input.length).toBe(0);
            });
        });

    });
    function getMockMeta() {
        return Object.freeze({
            "mock_number":   {
                "type":      "integer",
                "required":  true,
                "read_only": false,
                "label":     "Mock Integer",
                "min_value": 0,
                "max_value": 2147483647,
                "name":      "mock_number"
            },
            "mock_text":     {
                "type":       "string",
                "required":   false,
                "read_only":  false,
                "label":      "Mock Text",
                "max_length": 128,
                "name":       "mock_text"
            },
            "mock_textarea": {
                "type":      "string",
                "required":  false,
                "read_only": false,
                "label":     "Mock Textarea",
                "name":      "mock_textarea"
            }
        });
    }
})();
