class radioGroupDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/components/formControls/radioGroup.html',
      controller: radioGroupController,
      controllerAs: 'vm',
      scope: {
        value: '=ngModel',
        name: '=',
        meta: '='
      }
    };
    return directive;
  }
}

class radioGroupController {
  constructor($scope, $log) {
    'ngInject';

    this.$log = $log;
  }

}

export default radioGroupDirective;
