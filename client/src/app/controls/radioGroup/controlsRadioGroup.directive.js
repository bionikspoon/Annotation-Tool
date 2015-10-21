(function() {
  'use strict';

  // radioGroup
  angular
    .module('app.controls')
    .directive('appRadioGroup', controlsRadioGroupDirective);

  /** @ngInject **/
  function controlsRadioGroupDirective() {
    var directive = {
      bindToController: true,
      controller:       controlsRadioGroupController,
      controllerAs:     'vm',
      link:             link,
      restrict:         'E',
      templateUrl:      'app/controls/radioGroup/controlsRadioGroup.html',
      scope:            {}
    };
    return directive;

    function link(scope, element, attrs) {

    }
  }

  /** @ngInject **/
  function controlsRadioGroupController() {
    var vm = this;

    activate();

    ////////////////

    function activate() {

    }
  }

})();

