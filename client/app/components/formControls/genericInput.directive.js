class genericInputDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/components/formControls/genericInput.html',
      controller: genericInputController,
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

class genericInputController {
  constructor($scope, $log) {
    'ngInject';

    this.$log = $log;
    $scope.fieldType = genericInputController.getFieldType($scope);
  }

  static getFieldType($scope) {
    return $scope.meta.type === 'integer' ? 'number' : 'text';
  }
}

export default genericInputDirective;
