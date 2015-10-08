function radioGroupDirective() {
  'ngInject';

  const directive = {
    restrict: 'E',
    templateUrl: 'app/controls/radioGroup/radioGroup.html',
    controller: radioGroupController,
    controllerAs: 'field',
    bindToController: true,
    scope: {model: '=ngModel'},
    require: '^appFormMeta',
    link: link
  };
  return directive;
  function link(scope, element, attrs, ctrl) {
    const field = attrs.ngModel.split('.')
      .slice(-1)[0];

    scope.field.meta = ctrl.meta()[field];
    scope.field.form = ctrl.form;
  }

}

class radioGroupController {
  constructor($log, $timeout) {
    'ngInject';
    $timeout(this.$log = $log);
    this.clearButtonVisible = false;

  }

  showClear() {

    this.clearButtonVisible = true;
  }
  hideClear() {

    this.clearButtonVisible = false;
  }

}

export default radioGroupDirective;
