(function() {
  'use strict';

  // choiceSlider
  angular
    .module('app.controls')
    .directive('appChoiceSlider', controlsChoiceSliderDirective);

  /** @ngInject **/
  function controlsChoiceSliderDirective($mdMedia) {
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

    function link(scope, element, attrs) {

    }
  }

  /** @ngInject **/
  function controlsChoiceSliderController($mdMedia, $scope) {
    var vm = this;

    activate();

    ////////////////

    function activate() {

    }
  }

})();

