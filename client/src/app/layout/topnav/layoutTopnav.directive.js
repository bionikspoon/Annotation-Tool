(function() {
  'use strict';

  angular
    .module('app.layout')
    .directive('appTopnav', appTopnav);

  /* @ngInject */
  function appTopnav() {
    var directive = {
      bindToController: true,
      controller: TopnavController,
      controllerAs: 'vm',
      restrict: 'E',
      templateUrl: 'app/layout/topnav/layoutTopnav.html',
      scope: {}
    };
    return directive;
  }

  /* @ngInject */
  function TopnavController($mdSidenav) {
    var vm = this;
    vm.toggleNavbarSide = toggleNavbarSide;

    function toggleNavbarSide() {
      $mdSidenav('left').toggle();
    }

  }

})();

