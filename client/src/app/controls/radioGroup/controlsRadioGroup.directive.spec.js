(function() {
    'use strict';

    describe('controlsRadioGroup.directive.spec', function() {
        var $compile;
        var $rootScope;
        var $scope;
        var mockMeta = getMockMeta();

        beforeEach(module('app.controls'));

        beforeEach(inject(function(_$compile_, _$rootScope_) {
            $compile = _$compile_;
            $rootScope = _$rootScope_;
            $scope = $rootScope.$new();
            $scope.meta = mockMeta;
        }));

        describe('Compiled Template', function() {
            var formElement;
            var radioGroupElement;
            var vm;

            beforeEach(function() {
                var template = '<form app-form-meta=meta name=testForm><app-radio-group ng-model="data.mock_radio_group"></app-radio-group></form>';
                formElement = $compile(template)($scope);
                radioGroupElement = formElement.find('app-radio-group');
                $scope.$digest();
                vm = radioGroupElement.controller('appRadioGroup');
            });

            describe('Clear Button', function() {

                it('should not have a clear button when model is undefined', function() {
                    var buttonElement = radioGroupElement.find('md-button');
                    expect(vm.model).toBeUndefined();
                    expect(buttonElement.length).toBeFalsy();

                });

                it('should have a clear button when model is defined', function() {
                    vm.model = "1";
                    $scope.$digest();
                    var buttonElement = radioGroupElement.find('button');
                    expect(buttonElement.length).toBe(1);
                    expect(buttonElement.html()).toContain('Clear');

                });

            });

            describe('Controller', function() {

                it('should have access to field meta object', function() {
                    expect(vm.meta).toBe(mockMeta.mock_radio_group);
                });
            });
        });

    });

    function getMockMeta() {
        return {
            "mock_radio_group": {

                "type":      "field",
                "required":  false,
                "read_only": false,
                "label":     "Mock Radio Group",
                "choices":   [
                    {
                        "display_name": "Choice 1",
                        "value":        "1"
                    },
                    {
                        "display_name": "Choice 2",
                        "value":        "2"
                    },
                    {
                        "display_name": "Choice 3",
                        "value":        "3"
                    }
                ],
                "name":      "mock_radio_group"
            }
        };
    }

})();
