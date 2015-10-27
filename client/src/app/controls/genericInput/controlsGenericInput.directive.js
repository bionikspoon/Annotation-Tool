(function() {
  'use strict';

  // genericInput
  angular
    .module('app.controls')
    .directive('appGenericInput', controlsGenericInputDirective);

  /** @ngInject **/
  function controlsGenericInputDirective(controlsUtils) {
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
      var locals = {
        scope:    scope,
        formMeta: formMeta,
        field:    field
      };

      scope.vm.meta = controlsUtils.fieldMeta.bind(locals)();
      scope.vm.form = controlsUtils.fieldForm.bind(locals)();

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

