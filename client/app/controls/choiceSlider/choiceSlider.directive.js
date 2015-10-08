function choiceSliderDirective() {
  'ngInject';

  const directive = {
    restrict: 'E',
    templateUrl: 'app/controls/choiceSlider/choiceSlider.html',
    controller: choiceSliderController,
    controllerAs: 'field',
    bindToController: true,
    scope: {model: '=ngModel'},
    require: '^appFormMeta',
    link: link
  };
  return directive;
  function link(scope, element, attrs, ctrl) {
    const field = attrs.ngModel.split('.')
      .slice(-1);
    scope.field.meta = ctrl.meta()[field];
    scope.field.form = ctrl.form;
  }
}


class choiceSliderController {
  constructor($log, $mdMedia, $scope) {
    'ngInject';

    $scope.$watch(()=>$mdMedia('gt-md'), gtMd => this.gtMd = gtMd);


    this.$log = $log;
  }

}

export default choiceSliderDirective;
