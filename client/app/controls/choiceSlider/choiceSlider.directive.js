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
