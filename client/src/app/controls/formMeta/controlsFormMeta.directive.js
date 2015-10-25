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
      }/*,
       link:             link*/
    };
    return directive;
    /*    function link(scope, element, attrs) {
     console.debug('controlsFormMeta.directive arguments:', arguments);
     }*/
  }

  /** @ngInject **/
  function controlsFormMetaController($q, $log, $scope, $timeout) {
    var vm = this;

    vm.form = $q.when(vm.form);

    activate();

    ////////////////

    function activate() {}

  }

})();

