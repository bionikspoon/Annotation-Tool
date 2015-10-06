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
        value: '=ngModel',
        name: '@',
        meta: '='
      }
    };
    return directive;
  }
}

class genericInputController {
  constructor($log) {
    'ngInject';

    this.$log = $log;
    this.fieldType = this.getFieldType();
  }

  getFieldType() {
    return this.meta.type === 'integer' ? 'number' : 'text';
  }
}

export default genericInputDirective;
