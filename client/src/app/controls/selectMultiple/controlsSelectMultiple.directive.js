(function() {
  'use strict';

  // selectMultiple
  angular
    .module('app.controls')
    .directive('appSelectMultiple', controlsSelectMultipleDirective);

  /** @ngInject **/
  function controlsSelectMultipleDirective() {
    var directive = {
      bindToController: true,
      controller:       controlsSelectMultipleController,
      controllerAs:     'vm',
      link:             link,
      restrict:         'A',
      templateUrl:      'app/controls/selectMultiple/controlsSelectMultiple.html',
      scope:            {}
    };
    return directive;

    function link(scope, element, attrs) {

    }
  }

  /** @ngInject **/
  function controlsSelectMultipleController() {
    var vm = this;

    activate();

    ////////////////

    function activate() {

    }
  }

})();

