class selectMultipleDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/components/formControls/selectMultiple.html',
      controller: selectMultipleController,
      controllerAs: 'ctrl',
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

class selectMultipleController {
  constructor($log) {
    'ngInject';
    this.$log = $log;
    this.activate();
    this.selectedItem = null;
    this.searchText = null;
    this.value = this.value || [];
  }


  activate() {
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
