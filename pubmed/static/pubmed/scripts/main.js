(function ($) {
  /**
   *
   * jquery utility, filter inputs by value.
   * */
  $.fn.filterValue = function (value) {
    return this.filter(//
      function (index, $el) {
        return ($el.value === value.toString());
      });
  }
})(jQuery);

$(function () {


  var $form = $('#entry-form');

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
  // all select boxes for select2
  var $select2 = $form.find('select');


  /**
   *
   * Bind to form.
   * */
    //watch for changes to treatment radio select field
  $treatmentRadio.change(showFields);
  //init select2
  $select2.select2({
    theme: 'bootstrap'
  });

  /**
   *
   * Form Methods
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
});

$(function () {

  var $form = $('#entry-form');

  var $columnDiv = $form.find('div[data-form-column=True] > div').find('label.col-xs-4.col-md-3.col-lg-2', 'div.col-xs-8.col-md-9.col-lg-10');

  $columnDiv.hide();
});