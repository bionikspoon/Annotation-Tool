(function() {
  'use strict';

  // genericInput
  angular
    .module('app.controls')
    .directive('appGenericInput', controlsGenericInputDirective);

  /** @ngInject **/
  function controlsGenericInputDirective($log, $q, $timeout) {
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

      scope.vm.meta = fieldMeta(field);

      scope.vm.form = $q.when(formMeta.form);

      $timeout(function() {
        $log.debug('controlsGenericInput.directive scope.vm:', scope.vm);
      }, 1000);

      function fieldMeta(field) {
        return $q.when(formMeta.meta)
                 .then(function(meta) {
                   scope.vm.meta = meta[field];
                   return meta[field];
                 })
                 .catch(function(error) {
                   $log.error('controlsGenericInput.directive error:', error);
                 });
      }
    }

  }

  /** @ngInject **/
  function controlsGenericInputController($log, $timeout) {
    var vm = this; // jshint ignore:line
    activate();

    ////////////////

    function activate() {
      $timeout(function() {
        $log.debug('controlsGenericInput.directive vm:', vm);

      });
      //$log.debug('controlsGenericInput.directive vm:', vm);
    }
  }

})();

