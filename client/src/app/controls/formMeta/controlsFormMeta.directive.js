(function() {
  'use strict';

  // formMeta
  angular
    .module('app.controls')
    .directive('appFormMeta', controlsFormMetaDirective);

  /** @ngInject **/
  function controlsFormMetaDirective() {
    var directive = {
      bindToController: true,
      controller:       controlsFormMetaController,
      controllerAs:     'vm',
      restrict:         'A',
      scope:            {
        meta: '=appFormMeta',
        form: '=name'
      }
    };
    return directive;
  }

  /** @ngInject **/
  function controlsFormMetaController($q) {
    var vm = this;

    vm.form = $q.when(vm.form);

    activate();

    ////////////////

    function activate() {}

  }
})();

