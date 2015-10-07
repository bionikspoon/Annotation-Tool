function radioGroupDirective() {
  'ngInject';

  const directive = {
    restrict: 'E',
    templateUrl: 'app/controls/radioGroup/radioGroup.html',
    controller: radioGroupController,
    controllerAs: 'vm',
    bindToController: true,
    scope: {model: '=ngModel'},
    require: '^appFormMeta',
    link: link
  };
  return directive;
  function link(scope, element, attrs, meta) {
    const field = attrs.ngModel.split('.')
      .slice(-1);
    scope.vm.meta = meta[field];
  }

}

class radioGroupController {
  constructor($log, $timeout) {
    'ngInject';
    $timeout(this.$log = $log);

  }

}

export default radioGroupDirective;
