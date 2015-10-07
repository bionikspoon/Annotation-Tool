class choiceSliderDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/controls/choiceSlider/choiceSlider.html',
      controller: choiceSliderController,
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

class choiceSliderController {
  constructor($log) {
    'ngInject';

    this.$log = $log;
  }

}

export default choiceSliderDirective;
