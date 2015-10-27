(function() {
  'use strict';

  // radioGroup
  angular
    .module('app.controls')
    .directive('appRadioGroup', controlsRadioGroupDirective);

  /** @ngInject **/
  function controlsRadioGroupDirective(controlsUtils) {
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
  function controlsRadioGroupController() {
    //var vm = this;
    //activate();
    //
    //////////////////
    //
    //function activate() {}
  }

})();

