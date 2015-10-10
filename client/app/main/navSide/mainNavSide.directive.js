class NavbarSideDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/main/navSide/mainNavSide.html',
      controller: NavbarSideController,
      controllerAs: 'navSideCtrl',
      bindToController: true
    };

    return directive;
  }
}

class NavbarSideController {
  constructor() {
    'ngInject';

    this.openMenu = angular.bind(this, this.openMenu);
    return this;

  }

  openMenu($mdOpenMenu, $event) {
    $mdOpenMenu($event);
  }

}

export default NavbarSideDirective;