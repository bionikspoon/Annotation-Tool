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
   *****************************************************************************
   * */
  var $form = $('#entry-form');


  /**
   *
   * Module Definitions
   *****************************************************************************
   * */
  var treatmentBehavior = function ($form) {
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
  };

  var chromosomeStyles = function ($form) {
    /**
     *
     * Query main element
     * */
    var $formGroup = $form.find('[data-form-column=true] .form-group');

    /**
     *
     * Hack Styles
     * */
    $formGroup.find('*')//
      .removeClass('col-xs-4 col-md-3 col-lg-2 col-xs-8 col-md-9 col-lg-10');
    $formGroup.find('input.form-control')//
      .css('width', '95%')
  };

  var select2Init = function ($form) {
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

  };


  /**
   *
   * Impressively well organized modules.
   *****************************************************************************
   * */
  treatmentBehavior($form);
  chromosomeStyles($form);
  select2Init($form);
});

