function radioGroupDirective($log) {
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
    const field = attrs.ngModel.split('.').slice(-1)[0];

    ctrl.then(data => {
          scope.field.meta = data.meta[field];
          scope.field.form = data.form;
          return data;
        })
        .catch(error => $log.error('radioGroup.directive error:', error));
  }

}

class radioGroupController {
  constructor($log) {
    'ngInject';

    this.$log = $log;
    this.meta = this.meta || {};
    this.form = this.form || {};


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
