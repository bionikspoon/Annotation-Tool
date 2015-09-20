(function ($) {
    /**
     *
     * jQuery utility, filter inputs by value.
     * */
    $.fn.filterValue = function (value) {
        return this.filter(//
            function (index, $el) {
                return ($el.value === value.toString());
            });
    };


})(jQuery);

$(function () {
        /**
         *
         * Main DOM Node
         ***************************************************************************
         * */
        var $form = $('#entry-form');


        /**
         *
         * Impressively well organized modules.
         ***************************************************************************
         * */

        treatmentBehavior($form);
        //select2Setup($form);
        pubmedLookup($form);
        //formUI($form);

        /**
         *
         * Module Definitions
         ***************************************************************************
         * */
        function treatmentBehavior($form) {
            /**
             *
             * Elements of Interest
             * */
            // Select box for # of arms
            var $treatmentRadio = $form.find('input[type=radio][name=treatment]');
            // List of treatment field containers
            var $treatmentsFieldDivs = [
                $form.find('#div_id_treatment_1'),
                $form.find('#div_id_treatment_2'),
                $form.find('#div_id_treatment_3'),
                $form.find('#div_id_treatment_4'),
                $form.find('#div_id_treatment_5')
            ];


            /**
             *
             * Bind to form.
             * */
                //watch for changes to treatment radio select field
            $treatmentRadio.change(showFields);

            /**
             *
             * Module Methods
             * */
            function init() {

                //Find last filled treatment, skipping blanks. Default 1.
                var numberOfTreatments = $treatmentsFieldDivs.reduce(//
                    //reduce cb.
                    function (previousValue, $div, index) {
                        var $field = $div.find('input[type=text]');

                        return $field.val() ? ++index : previousValue;
                    }, 1);

                //Click radio select for corresponding number of treatments.
                $treatmentRadio.filterValue(numberOfTreatments).click();
            }

            //Show fields for selected number of treatments, hide the rest.
            function showFields(e) {
                var fields = e.target.value;

                //Show fields.
                $treatmentsFieldDivs.slice(0, fields).map(function (treatment) {
                        treatment.show();
                    });

                //Hide the rest.
                $treatmentsFieldDivs.slice(fields).map(function (treatment) {
                        treatment.hide();
                    });
            }

            /**
             *
             * Initialize Module
             * */
            init();
        }

        function formUI($form) {
            $form.find(':radio').radiocheck();
            $form.find('select').select2();
        }


        function select2Setup($form) {
            /**
             *
             * Query all select boxes for select2
             * */
            var $select2 = $form.find('select');

            //noinspection JSUnresolvedFunction
            /**
             *
             * Initialize Select 2
             * */
            $select2.select2({
                    theme: 'bootstrap'
                });

        }

        function pubmedLookup($form) {

            var _summary = [];
            var _results = null;
            /**
             *
             * Queries of interest.
             * */
            var $pubmedId = $form.find('#id_pubmed_id');
            var $summaryDiv = $form.find('#hint_id_pubmed_id');
            var $resultsDiv = $form.find('#results');
            var entryId = $form.find('#id_id').val();

            /**
             *
             * Bind to DOM
             * */

            $pubmedId.keyup(getEntriesResults);

            /**
             *
             * Methods
             * */

            function getEntriesResults(e) {
                var pubmedId = (typeof e === "string") ? e : e.target.value;
                var payload = {'pubmed_id': pubmedId};
                if (entryId) {
                    payload['exclude__entry'] = entryId

                }

                if (pubmedId) {
                    $.get('/api/pubmed/html/', payload, setResults)
                } else {
                    setResults(false);
                }
            }


            function setResults(response, _, jqXHR) {
                if (response) {
                    jqXHR

                        .done(function (response) {

                            _results = response ? response : '';
                            _summary = jqXHR.getResponseHeader('count');
                        })

                        .fail(function () {

                        })

                        .always(function () {
                            renderSummaryMessage();
                            toggleSummaryVisibility();
                            renderResults();

                        });
                }


            }

            function toggleSummaryVisibility() {
                if (_summary.length) {
                    $resultsDiv.show();
                } else {
                    $resultsDiv.hide();
                }

            }

            function renderSummaryMessage() {
                var adjective = _summary.toString();
                var noun = (_summary === 1 ? ' pubmed entry found.'
                    : ' pubmed entries found.');
                var verb = _summary > 0 ? ' <a href=#results>Jump</a>' : '';

                $summaryDiv.html(adjective + noun + verb);
            }

            function renderResults() {
                var jump = '<p><a href=#entry-form>Jump</a></p>';

                $resultsDiv.html(jump + _results);
            }


            /**
             *
             * Initialization
             * */

            getEntriesResults($pubmedId.val());


        }


    });

