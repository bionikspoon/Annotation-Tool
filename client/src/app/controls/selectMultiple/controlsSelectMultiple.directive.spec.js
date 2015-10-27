(function() {
    'use strict';

    describe('controlsSelectMultiple.directive.spec', function() {
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
            var selectMultipleElement;
            var vm;

            beforeEach(function() {
                var template = '<form app-form-meta=meta name=testForm><app-select-multiple ng-model=data.mock_select_multiple></app-select-multiple></form>';
                formElement = $compile(template)($scope);
                selectMultipleElement = formElement.find('app-select-multiple');
                $scope.$digest();
                vm = selectMultipleElement.controller('appSelectMultiple');
            });

            it('should render directive', function() {
                expect(formElement.length).toBe(1);
                expect(selectMultipleElement.length).toBe(1);

            });

            describe('Controller', function() {

                it('should have keys', function() {
                    var controllerKeys = [
                        'model',
                        'selectedItem',
                        'searchText',
                        'modelOptions',
                        'querySearch',
                        'appendModel',
                        'getChipDisplayName',
                        'meta',
                        'form',
                        '_choices',
                        'ngModel'
                    ];
                    expect(Object.keys(vm)).toEqual(controllerKeys);
                });

                it('should have access to field meta object', function() {
                    expect(vm.meta).toBe(mockMeta.mock_select_multiple);
                });

                describe('appendModel', function() {

                    it('should return choices value', function() {
                        expect(vm.appendModel(vm._choices['id:1'])).toBe('id:1');
                    });
                });

                describe('getChipDisplayName', function() {

                    it('should return chips display name', function() {
                        expect(vm.getChipDisplayName('id:1')).toBe('Choice 1');
                    });
                });

                describe('vm._choices', function() {

                    it('should be an object', function() {
                        expect(angular.isObject(vm._choices)).toBeTruthy();
                    });

                    it('should be a key value map', function() {
                        var choice = {
                            "display_name":        "Choice 1",
                            "value":               "id:1",
                            "_lower_display_name": "choice 1"
                        };
                        expect(vm._choices["id:1"]).toEqual(choice);
                    });

                    it('should have keys of meta.choice values', function() {
                        var choiceKeys = [
                            'id:1',
                            'id:2',
                            'id:3',
                            'id:4',
                            'id:5'
                        ];
                        expect(Object.keys(vm._choices)).toEqual(choiceKeys);
                    });
                });

                describe('querySearch', function() {

                    beforeEach(function() {
                        vm.model = ['id:4'];
                        $rootScope.$apply();
                    });

                    it('should return non selected matching choices', function() {
                        var query = 'choices';
                        var results = vm.querySearch(query);
                        var expected = [
                            {
                                "display_name":        "Choices 5",
                                "value":               "id:5",
                                "_lower_display_name": "choices 5"
                            }
                        ];

                        expect(results).toEqual(expected);

                    });
                });

            });
        });

    });

    function getMockMeta() {
        return {
            "mock_select_multiple": {
                "type":      "field",
                "required":  false,
                "read_only": false,
                "label":     "Mock Select Multiple",
                "name":      "mock_select_multiple",
                "choices":   [
                    {
                        "display_name": "Choice 1",
                        "value":        "id:1"
                    },
                    {
                        "display_name": "Choice 2",
                        "value":        "id:2"
                    },
                    {
                        "display_name": "Choice 3",
                        "value":        "id:3"
                    },
                    {
                        "display_name": "Choices 4",
                        "value":        "id:4"
                    },
                    {
                        "display_name": "Choices 5",
                        "value":        "id:5"
                    }
                ]
            }
        };
    }

})();
