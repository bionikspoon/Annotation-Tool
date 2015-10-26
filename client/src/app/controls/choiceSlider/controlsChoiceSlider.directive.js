(function() {
  'use strict';

  // choiceSlider
  angular
    .module('app.controls')
    .directive('appChoiceSlider', controlsChoiceSliderDirective);

  /** @ngInject **/
  function controlsChoiceSliderDirective() {
    var directive = {
      bindToController: true,
      controller:       controlsChoiceSliderController,
      controllerAs:     'vm',
      link:             link,
      restrict:         'E',
      templateUrl:      'app/controls/choiceSlider/controlsChoiceSlider.html',
      scope:            {}
    };
    return directive;

    function link(scope, element, attrs) { // jshint ignore:line

    }
  }

  /** @ngInject **/
  function controlsChoiceSliderController() {
    var vm = this; // jshint ignore:line

    activate();

    ////////////////

    function activate() {

    }
  }

})();

