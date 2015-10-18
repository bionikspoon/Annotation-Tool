export default class SidenavDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/main/sidenav/mainSidenav.html',
      controller: SidenavController,
      controllerAs: 'sidenavCtrl',
      bindToController: true
    };

    return directive;
  }
}

class SidenavController {
  constructor($scope) {
    'ngInject';

    this.openMenu = angular.bind(this, this.openMenu);
    this.navLinks = [
      {
        data: {
          route: 'pubmed.list',
          icon: 'home',
          label: 'Home',
          condition: () => true
        }
      }, {
        data: {
          route: 'pubmed.list',
          icon: 'crop',
          label: 'Pubmed',
          condition: () => true
        }
      }, {
        data: {
          route: 'users.list',
          icon: 'people',
          label: 'Users',
          condition: $scope.userCtrl.isAuthenticated
        }
      }
    ];
  }

  openMenu($mdOpenMenu, $event) {
    $mdOpenMenu($event);
  }

}
