function genericInputDirective($log) {
  'ngInject';

  const directive = {
    restrict: 'E',
    templateUrl: 'app/controls/genericInput/genericInput.html',
    controller: genericInputController,
    controllerAs: 'vm',
    bindToController: true,
    scope: {ngModel: '=ngModel'},
    require: ['^appFormMeta', '^form'],
    link: link
  };
  return directive;

  function link(scope, element, attrs, controllers) {
    const [meta, form] = controllers;
    $log.debug('genericInput.directive scope:', scope);
    $log.debug('genericInput.directive form:', form);
    const field = attrs.ngModel.split('.')
      .slice(-1);
    scope.vm.meta = meta[field];
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
