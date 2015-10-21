(function() {
  'use strict';

  // genericInput
  angular
    .module('app.controls')
    .directive('appGenericInput', controlsGenericInputDirective);

  /** @ngInject **/
  function controlsGenericInputDirective() {
    var directive = {
      bindToController: true,
      controller:       controlsGenericInputController,
      controllerAs:     'vm',
      restrict:         'E',
      scope:            {model: '=ngModel'},
      templateUrl:      'app/controls/genericInput/controlsGenericInput.html',
      link:             link
    };
    return directive;

    function link(scope, element, attrs) { // jshint ignore:line

    }
  }

  /** @ngInject **/
  function controlsGenericInputController() {
    var vm = this; // jshint ignore:line

  }

})();

