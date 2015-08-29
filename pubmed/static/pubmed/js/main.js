$(function () {


  var $form = $('#entry-form');

  /**
   *
   * Elements of Interest
   * */
  // Select box for # of arms
  var $treatmentSelect = $form.find('#id_treatment');
  // List of treatment fields
  var $treatmentsFields = [
    $form.find('#div_id_treatment_1'),
    $form.find('#div_id_treatment_2'),
    $form.find('#div_id_treatment_3'),
    $form.find('#div_id_treatment_4'),
    $form.find('#div_id_treatment_5')
  ];
  var $select2 = $form.find('select');


  /**
   *
   * Bind to form.
   * */
  $treatmentSelect.change(showFields);
  $select2.select2({
    theme: 'bootstrap'
  });

  /**
   *
   * Form Methods
   * */
  function init() {
    showFields(1);
  }

  function showFields(e) {
    var fields;
    if (typeof e === 'number') {
      fields = e;
    } else {
      fields = e.target.value
    }

    $treatmentsFields.slice(0, fields).map(function (treatment) {
      treatment.show();
    });

    $treatmentsFields.slice(fields).map(function (treatment) {
      treatment.hide();
    });
  }

  /**
   *
   * Initialize Module
   * */
  init();
});