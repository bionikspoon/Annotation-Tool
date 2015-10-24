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

      scope.vm.meta = formMeta.meta[field];
      scope.vm.form = formMeta.form;
      //$log.debug('controlsGenericInput.directive scope.vm:', scope.vm);

    }
  }

  /** @ngInject **/
  function controlsGenericInputController($log) {
    var vm = this; // jshint ignore:line
    activate();

    ////////////////

    function activate() {
      //$log.debug('controlsGenericInput.directive vm:', vm);
    }
  }

})();

