class genericInputDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/components/formControls/genericInput.html',
      controller: genericInputController,
      controllerAs: 'vm'
    };

    return directive;
  }
}

class genericInputController {
  constructor() {
    'ngInject';

  }



}

export default genericInputDirective;
