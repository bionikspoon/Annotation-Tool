function formMetaDirective($log) {
  'ngInject';

  let directive = {
    restrict: 'A',
    controller: FormMetaController,
    controllerAs: 'form',
    bindToController: true,
    scope: {
      meta: '&appFormMeta'
    }
  };
  return directive;
}


class FormMetaController {
  constructor($log ) {
    'ngInject';
    return this.meta();

  }
}

export default formMetaDirective;
