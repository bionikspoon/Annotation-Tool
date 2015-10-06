class selectMultipleDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/components/formControls/selectMultiple.html',
      controller: selectMultipleController,
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

class selectMultipleController {
  constructor($log) {
    'ngInject';

    this.$log = $log;
  }

}

export default selectMultipleDirective;
