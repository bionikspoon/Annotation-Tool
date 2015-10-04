class NavbarSideDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/components/navbarSide/navbarSide.html',
      controller: NavbarSideController,
      controllerAs: 'vm',
      bindToController: true
    };

    return directive;
  }
}

class NavbarSideController {
  constructor() {
    'ngInject';

  }

}

export default NavbarSideDirective;
