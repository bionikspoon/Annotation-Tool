/* global _:false */
(function() {
    'use strict';

    describe('controlsUtils.factory.spec', function() {
        var controlsUtils;

        beforeEach(module('app.controls'));

        beforeEach(inject(function(_controlsUtils_) {
            controlsUtils = _controlsUtils_;
        }));

        it('Should have a public api', function() {
            var keys = [
                'factoryFilterExcludeSelected',
                'factoryFilterLowercase',
                'prepareChoices',
                'fieldMeta',
                'fieldForm'
            ];
            expect(Object.keys(controlsUtils)).toEqual(keys);
        });

        describe('When filtering to exclude selected', function() {
            var choices;

            beforeEach(function() {
                choices = getChoices().expected;
            });

            it('Should exclude selected ' + '' + 'items', function() {
                // All choices except `id:5`
                var selected = [
                    'id:1',
                    'id:2',
                    'id:3',
                    'id:4'
                ];
                var results = _.valuesIn(choices)
                               .filter(controlsUtils.factoryFilterExcludeSelected(selected));
                expect(results).toEqual([choices['id:5']]);

            });

            it('Should include all choices when none are selected', function() {
                var selected = [];
                var results = _.valuesIn(choices)
                               .filter(controlsUtils.factoryFilterExcludeSelected(selected));
                expect(results).toEqual(_.valuesIn(choices));
            });

            it('Should return an empty list when all are selected', function() {
                var selected = [
                    'id:1',
                    'id:2',
                    'id:3',
                    'id:4',
                    'id:5'
                ];
                var results = _.valuesIn(choices)
                               .filter(controlsUtils.factoryFilterExcludeSelected(selected));
                expect(results).toEqual([]);
            });

        });

        describe('When filtering to search lowercase', function() {
            var choices;

            beforeEach(function() {
                choices = getChoices().expected;
            });

            it('Should search a choices lowercase display name', function() {
                var query = 'choice 1';
                var results = _.valuesIn(choices)
                               .filter(controlsUtils.factoryFilterLowercase(query));
                expect(results).toEqual([choices['id:1']]);
            });

            // QUADRUPLE negative!!!!!!!!
            it('Should not exclude non disqualifiers', function() {
                var query = 'choice';
                var results = _.valuesIn(choices)
                               .filter(controlsUtils.factoryFilterLowercase(query));
                expect(results).toEqual(_.valuesIn(choices));
            });

            it('Should only include matches', function() {
                var query = 'choices';
                var results = _.valuesIn(choices)
                               .filter(controlsUtils.factoryFilterLowercase(query));
                var expected = [
                    choices['id:4'],
                    choices['id:5']
                ];
                expect(results).toEqual(expected);

            });

            it('Should not exclude anything if query is empty', function() {
                var query = '';
                var results = _.valuesIn(choices)
                               .filter(controlsUtils.factoryFilterLowercase(query));
                expect(results).toEqual(_.valuesIn(choices));

            });
        });

        describe('prepareChoices', function() {

            it('Should prepare choices', function() {
                var choices = getChoices();
                expect(controlsUtils.prepareChoices(choices.actual)).toEqual(choices.expected);
            });

        });
    });

    function getChoices() {
        var actual = [
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
        ];
        var expected = {
            "id:1": {
                "display_name":        "Choice 1",
                "value":               "id:1",
                "_lower_display_name": "choice 1"
            },
            "id:2": {
                "display_name":        "Choice 2",
                "value":               "id:2",
                "_lower_display_name": "choice 2"
            },
            "id:3": {
                "display_name":        "Choice 3",
                "value":               "id:3",
                "_lower_display_name": "choice 3"
            },
            "id:4": {
                "display_name":        "Choices 4",
                "value":               "id:4",
                "_lower_display_name": "choices 4"
            },
            "id:5": {
                "display_name":        "Choices 5",
                "value":               "id:5",
                "_lower_display_name": "choices 5"
            }
        };
        return Object.freeze({
            actual:   actual,
            expected: expected
        });
    }

})();
