class choiceSliderDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/components/formControls/choiceSlider.html',
      controller: choiceSliderController,
      controllerAs: 'vm',
      scope: {
        value: '=ngModel',
        name: '@',
        meta: '='
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
