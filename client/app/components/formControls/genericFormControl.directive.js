class genericFormControlDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/components/formControls/genericFormControl.html',
      controller: genericFormControlController,
      controllerAs: 'vm'
    };

    return directive;
  }
}

class genericFormControlController {
  constructor() {
    'ngInject';

  }



}

export default genericFormControlDirective;
