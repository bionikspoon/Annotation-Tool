(function() {
  'use strict';

  // choiceSlider
  angular
    .module('app.controls')
    .directive('appChoiceSlider', controlsChoiceSliderDirective);

  /** @ngInject **/
  function controlsChoiceSliderDirective($mdMedia, controlsUtils) {
    var directive = {
      bindToController: true,
      controller:       controlsChoiceSliderController,
      controllerAs:     'vm',
      link:             link,
      restrict:         'E',
      templateUrl:      'app/controls/choiceSlider/controlsChoiceSlider.html',
      scope:            {model: '=ngModel'},
      require:          '^appFormMeta'
    };
    return directive;

    function link(scope, element, attrs, formMeta) {
      var field = attrs.ngModel
                       .split('.')
                       .slice(-1)[0];
      var locals = {
        scope:    scope,
        formMeta: formMeta,
        field:    field
      };

      scope.vm.meta = controlsUtils.fieldMeta.apply(locals);
      scope.vm.form = controlsUtils.fieldForm.apply(locals);

      scope.$watch(watchMdMedia, setGtMd);

      function watchMdMedia() {
        return $mdMedia('gt-md');
      }

      function setGtMd(gtMd) {
        scope.vm.gtMd = gtMd;
      }
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

