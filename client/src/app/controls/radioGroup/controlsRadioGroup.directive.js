(function() {
  'use strict';

  // radioGroup
  angular
    .module('app.controls')
    .directive('appRadioGroup', controlsRadioGroupDirective);

  /** @ngInject **/
  function controlsRadioGroupDirective($log, $q) {
    var directive = {
      bindToController: true,
      controller:       controlsRadioGroupController,
      controllerAs:     'vm',
      link:             link,
      restrict:         'E',
      templateUrl:      'app/controls/radioGroup/controlsRadioGroup.html',
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
  function controlsRadioGroupController() {
    //var vm = this;
    //activate();
    //
    //////////////////
    //
    //function activate() {}
  }

})();

