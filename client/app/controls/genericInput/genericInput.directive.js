function genericInputDirective($log) {
  'ngInject';

  const directive = {
    restrict: 'E',
    templateUrl: 'app/controls/genericInput/genericInput.html',
    controller: genericInputController,
    controllerAs: 'field',
    bindToController: true,
    scope: {model: '=ngModel'},
    require: '^appFormMeta',
    link: link
  };
  return directive;

  function link(scope, element, attrs, form) {
    const field = attrs.ngModel.split('.')
      .slice(-1);
    scope.field.meta = form[field];
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
