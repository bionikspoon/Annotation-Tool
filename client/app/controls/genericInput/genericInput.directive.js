function genericInputDirective($log) {
  'ngInject';

  const directive = {
    restrict: 'E',
    templateUrl: 'app/controls/genericInput/genericInput.html',
    controller: genericInputController,
    controllerAs: 'field',
    bindToController: true,
    scope: {model: '=ngModel'},
    require: ['^appFormMeta', '?ngModel'],
    link: link
  };
  return directive;

  function link(scope, element, attrs, controllers) {
    const [ctrl, ngModel] = controllers;
    const field = attrs.ngModel.split('.')
      .slice(-1)[0];

    scope.field.meta = ctrl.meta()[field];
    scope.field.form = ctrl.form;

  }
}

class genericInputController {
  constructor($log) {
    'ngInject';
    this.$log = $log;

  }


}

export default genericInputDirective;
