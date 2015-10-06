class radioGroupDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/controls/radioGroup/radioGroup.html',
      controller: radioGroupController,
      controllerAs: 'vm',
      scope: {
        value: '=ngModel',
        name: '@',
        meta: '='
      }
    };
    return directive;
  }
}

class radioGroupController {
  constructor( $log) {
    'ngInject';

    this.$log = $log;
  }

}

export default radioGroupDirective;
