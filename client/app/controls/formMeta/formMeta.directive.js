class FormMetaDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'A',
      controller: FormMetaController,
      controllerAs: 'meta',
      bindToController: true,
      scope: {
        meta: '&appFormMeta'
      }

    };

    return directive;
  }
}

class FormMetaController {
  constructor() {
    'ngInject';
    return this.meta();
  }


}

export default FormMetaDirective;
