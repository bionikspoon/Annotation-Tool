(function() {
    'use strict';

    describe('controlsChoiceSlider.directive.spec', function() {
        var $compile;
        var $rootScope;
        var $scope;
        var mockMeta = getMockData();

        beforeEach(module('app.controls', 'mock.$mdMedia'));

        //beforeEach(module());

        beforeEach(inject(function(_$compile_, _$rootScope_) {
            $compile = _$compile_;
            $rootScope = _$rootScope_;
            $scope = $rootScope.$new();
            $scope.meta = mockMeta;
        }));

        describe('When compiled', function() {
            var formElement;
            var choiceSliderElement;
            var vm;

            beforeEach(function() {
                var template = '<form name=testForm app-form-meta=meta><app-choice-slider ng-model=data.mock_choice_slider></app-choice-slider></form>';
                formElement = $compile(template)($scope);
                choiceSliderElement = formElement.find('app-choice-slider');
                $scope.$digest();
                vm = choiceSliderElement.controller('appChoiceSlider');
            });

            it('Should render directive', function() {
                expect(formElement.length).toBe(1);
                expect(choiceSliderElement.length).toBe(1);
                expect(Object.keys(vm)).toEqual([
                    'model',
                    'meta',
                    'form',
                    'gtMd'
                ]);
            });

            it('Should compute max value from choices', function() {
                var mdSliderElement = choiceSliderElement.find('md-slider');
                expect(mdSliderElement.attr('max')).toBe('5');
                expect(mdSliderElement.attr('min')).toBe('0');

            });

            it('Should have number input and slider using the same model', function() {
                var input = choiceSliderElement.find('input');
                var mdSliderElement = choiceSliderElement.find('md-slider');
                expect(mdSliderElement.attr('ng-model')).toBe(input.attr('ng-model'));
            });

            describe('Inner Number Input', function() {
                var inputContainerElement;
                var $mdMedia;

                beforeEach(inject(function(_$mdMedia_) {
                    $mdMedia = _$mdMedia_;
                    inputContainerElement = choiceSliderElement.find('md-input-container');
                }));

                it('Should use populate label from meta', function() {
                    var label = inputContainerElement.find('label');
                    expect(label.html()).toContain(mockMeta.mock_choice_slider.label);
                });

                it('Should have a matching label and input id', function() {
                    var label = inputContainerElement.find('label');
                    var input = inputContainerElement.find('input');

                    expect(input.attr('id')).toBe(label.attr('for'));
                });

                it('Should not have css class "gtMd"', function() {
                    var input = inputContainerElement.find('input');
                    expect(input.hasClass('gt-md')).toBeFalsy();
                });

                it('Should have css class "gtMd"', function() {
                    $mdMedia.return = true;
                    $rootScope.$apply();
                    var input = inputContainerElement.find('input');
                    expect(input.hasClass('gt-md')).toBeTruthy();
                });

            });

            describe('Controller', function() {

                it('Should have access to field meta', function() {
                    expect(vm.meta).toBe(mockMeta.mock_choice_slider);
                });
            });
        });

    });

    function getMockData() {
        return Object.freeze({
            "mock_choice_slider": {
                "type":      "choice",
                "required":  false,
                "read_only": false,
                "label":     "Mock Choice Slider",
                "name":      "mock_choice_slider",
                "choices":   [
                    {
                        "display_name": 1,
                        "value":        1
                    },
                    {
                        "display_name": 2,
                        "value":        2
                    },
                    {
                        "display_name": 3,
                        "value":        3
                    },
                    {
                        "display_name": 4,
                        "value":        4
                    },
                    {
                        "display_name": 5,
                        "value":        5
                    }
                ]
            }
        });
    }

})();
