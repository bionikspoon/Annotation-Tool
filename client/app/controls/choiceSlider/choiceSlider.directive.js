function choiceSliderDirective($log) {
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
    const field = attrs.ngModel.split('.').slice(-1)[0];

    ctrl.then(data => {
          scope.field.meta = data.meta[field];
          scope.field.form = data.form;
          return data;
        })
        .catch(error => $log.error('choiceSlider.directive error:', error));
  }
}


class choiceSliderController {
  constructor($log, $mdMedia, $scope) {
    'ngInject';

    this.$log = $log;
    this.meta = this.meta || {};
    this.form = this.form || {};

    this.activate($mdMedia, $scope);
  }

  activate($mdMedia, $scope) {
    $scope.$watch(()=>$mdMedia('gt-md'), gtMd => this.gtMd = gtMd);
  }

}

export default choiceSliderDirective;
