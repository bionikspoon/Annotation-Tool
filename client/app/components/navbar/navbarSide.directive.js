class NavbarSideDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/components/navbar/navbarSide.html',
      controller: NavbarSideController,
      controllerAs: 'vm'
    };

    return directive;
  }
}

class NavbarSideController {
  constructor() {
    'ngInject';

  }

  openMenu($mdOpenMenu, $event) {
    $mdOpenMenu($event);
  }

}

export default NavbarSideDirective;
