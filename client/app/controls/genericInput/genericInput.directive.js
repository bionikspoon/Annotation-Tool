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

  function link(scope, element, attrs, ctrl) {
    const field = attrs.ngModel.split('.')
      .slice(-1)[0];


    ctrl.then(data => {
        scope.field.meta = data.meta[field];
        scope.field.form = data.form;
        return data;
      })
      .catch(error=>$log.error('genericInput.directive error:', error));

  }
}

class genericInputController {
  constructor($log) {
    'ngInject';
    this.$log = $log;
    this.meta = this.meta || {};
    this.form = this.form || {};
  }
}

export default genericInputDirective;
