class radioGroupDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/controls/radioGroup/radioGroup.html',
      controller: radioGroupController,
      controllerAs: 'vm',
      bindToController: true,
      scope: {
        field: '@',
        model: '=ngModel'
      },
      require: '^appFormMeta',
      link: (scope, element, attrs, meta) => {
        scope.vm.meta = meta[scope.vm.field];
      }
    };
    return directive;
  }
}

class radioGroupController {
  constructor($log, $timeout) {
    'ngInject';
    $timeout(this.$log = $log);

  }

}

export default radioGroupDirective;
