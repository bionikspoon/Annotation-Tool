class NavbarTopDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/components/navbar/navbarTop.html',
      controller: NavbarTopController,
      controllerAs: 'vm'
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
