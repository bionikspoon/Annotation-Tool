(function() {
  'use strict';

  // choiceSlider
  angular
    .module('app.controls')
    .directive('appChoiceSlider', controlsChoiceSliderDirective);

  /** @ngInject **/
  function controlsChoiceSliderDirective($log, $q) {
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

      scope.vm.meta = fieldMeta();
      scope.vm.form = fieldForm();

      function fieldMeta() {
        return $q.when(formMeta.meta)
                 .then(function(meta) {
                   scope.vm.meta = meta[field];
                   return meta[field];
                 })
                 .catch(function(error) {
                   $log.error('controlsGenericInput.directive error:', error);
                   return $q.reject(error);
                 });
      }

      function fieldForm() {
        return $q.when(formMeta.form)
                 .then(function(form) {
                   scope.vm.form = form;
                   return form;
                 })
                 .catch(function(error) {
                   $log.error('controlsGenericInput.directive error:', error);
                   return $q.reject(error);
                 });
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

