export default class TopnavDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/main/topnav/mainTopnav.html',
      controller: TopnavController,
      controllerAs: 'topnavCtrl',
      bindToController: true,
      scope: {}
    };

    return directive;
  }
}

class TopnavController {
  constructor($mdSidenav) {
    'ngInject';

    this.$mdSidenav = $mdSidenav;
  }

  toggleNavbarSide() {
    this.$mdSidenav('left')
        .toggle();
  }
}

