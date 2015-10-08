class FormMetaDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'A',
      controller: FormMetaController,
      controllerAs: 'meta',
      bindToController: true,
      scope: {
        meta: '&appFormMeta',
        errors: '=appFormErrors'
      }
    };
    return directive;
  }
}

class FormMetaController {
  constructor() {
    'ngInject';

    return this.meta(); // jshint ignore:line
  }


}

export default FormMetaDirective;
