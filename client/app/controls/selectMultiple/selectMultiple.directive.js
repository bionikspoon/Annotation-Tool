function selectMultipleDirective() {
  'ngInject';

  const directive = {
    restrict: 'E',
    templateUrl: 'app/controls/selectMultiple/selectMultiple.html',
    controller: selectMultipleController,
    controllerAs: 'vm',
    bindToController: true,
    scope: {model: '=ngModel'},
    require: '^appFormMeta',
    link: link
  };
  return directive;
  function link(scope, element, attrs, meta) {
    const field = attrs.ngModel.split('.')
      .slice(-1);
    scope.vm.meta = meta[field];
  }
}


class selectMultipleController {
  constructor($log, $timeout) {
    'ngInject';
    $timeout(()=> {

      this.$log = $log;
      this.selectedItem = null;
      this.searchText = null;
      this.model = this.model || [];


      this.activate();

    });
  }


  activate() {
    this.$log.debug('selectMultiple.directive this.meta.choices:', this.meta);

    this.meta.choices = this.meta.choices.map(choice => {
      choice._lower_display_name = choice.display_name.toLowerCase();
      return choice;
    });

  }

  querySearch(query) {
    const results = query ? this.meta.choices.filter(this.createFilterFor(query)) : [];
    return results;
  }

  createFilterFor(query) {
    const lowercaseQuery = angular.lowercase(query);
    return function filterFn(choice) {
      return (choice._lower_display_name.indexOf(lowercaseQuery));
    };

  }


}

export default selectMultipleDirective;
