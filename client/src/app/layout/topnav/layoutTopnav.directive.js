(function() {
  'use strict';
  // Topnav
  angular
    .module('app.layout')
    .directive('appTopnav', layoutTopnavDirective);

  /* @ngInject */
  function layoutTopnavDirective() {
    var directive = {
      bindToController: true,
      controller:       layoutTopnavController,
      controllerAs:     'vm',
      restrict:         'E',
      templateUrl:      'app/layout/topnav/layoutTopnav.html',
      scope:            {}
    };
    return directive;

  }

  /* @ngInject */
  function layoutTopnavController() {
    var vm = this;
    vm.toggleNavbarSide = toggleNavbarSide;

    function toggleNavbarSide($mdSidenav) {
      $mdSidenav('left').toggle();
    }

  }

})();

