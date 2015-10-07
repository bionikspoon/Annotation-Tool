function choiceSliderDirective() {
  'ngInject';

  const directive = {
    restrict: 'E',
    templateUrl: 'app/controls/choiceSlider/choiceSlider.html',
    controller: choiceSliderController,
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


class choiceSliderController {
  constructor($log) {
    'ngInject';

    this.$log = $log;
  }

}

export default choiceSliderDirective;
