class NavbarTopDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/main/navTop/mainNavTop.html',
      controller: NavbarTopController,
      controllerAs: 'navTopCtrl'
    };

    return directive;
  }
}

class NavbarTopController {
  constructor($mdSidenav) {
    'ngInject';

    this.$mdSidenav = $mdSidenav;
  }

  toggleNavbarSide() {
    this.$mdSidenav('left')
        .toggle();
  }
}

export default NavbarTopDirective;
