function formMetaDirective($log) {
  'ngInject';

  let directive = {
    restrict: 'A',
    controller: FormMetaController,
    controllerAs: 'form',
    bindToController: true,
    scope: {
      meta: '&appFormMeta',
      form: '=name'
    }
  };
  return directive;
}


class FormMetaController {
  constructor() {
    'ngInject';
    const constructor = this.meta();
    constructor.form = this.form;
    return {form: this.form, meta: this.meta()};

  }
}

export default formMetaDirective;
