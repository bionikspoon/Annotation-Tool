class selectMultipleDirective {
  constructor() {
    'ngInject';

    let directive = {
      restrict: 'E',
      templateUrl: 'app/controls/selectMultiple/selectMultiple.html',
      controller: selectMultipleController,
      controllerAs: 'vm',
      bindToController: true,
      scope: {
        field: '@',
        model: '=ngModel'
      },
      require: '^appFormMeta',
      link: (scope, element, attrs, meta) => {
        scope.vm.meta = meta[scope.vm.field];
      }
    };
    return directive;
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
