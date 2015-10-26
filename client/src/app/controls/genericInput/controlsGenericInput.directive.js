(function() {
  'use strict';

  // genericInput
  angular
    .module('app.controls')
    .directive('appGenericInput', controlsGenericInputDirective);

  /** @ngInject **/
  function controlsGenericInputDirective($log, $q) {
    var directive = {
      bindToController: true,
      controller:       controlsGenericInputController,
      controllerAs:     'vm',
      restrict:         'E',
      scope:            {model: '=ngModel'},
      require:          '^appFormMeta',
      templateUrl:      'app/controls/genericInput/controlsGenericInput.html',
      link:             link
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
  function controlsGenericInputController() {
    //var vm = this;
    //activate();
    //
    //////////////////
    //
    //function activate() {}

  }

})();

