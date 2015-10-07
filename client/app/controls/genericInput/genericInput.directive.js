class genericInputDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/controls/genericInput/genericInput.html',
      controller: genericInputController,
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

class genericInputController {
  constructor($log, $timeout) {
    'ngInject';
    $timeout(()=> {
      this.$log = $log;
    });
  }


}

export default genericInputDirective;
