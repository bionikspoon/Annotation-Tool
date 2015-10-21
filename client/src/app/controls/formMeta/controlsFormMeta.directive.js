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
      scope:            {}
    };
    return directive;
  }

  /** @ngInject **/
  function controlsFormMetaController($q, $log, $scope, $timeout) {
    var vm = this;

  }

})();

