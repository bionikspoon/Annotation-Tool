function selectMultipleDirective($log) {
  'ngInject';

  const directive = {
    restrict: 'E',
    templateUrl: 'app/controls/selectMultiple/selectMultiple.html',
    controller: selectMultipleController,
    controllerAs: 'field',
    bindToController: true,
    scope: {model: '=ngModel'},
    require: '^appFormMeta',
    link: link
  };
  return directive;

  function link(scope, element, attrs, ctrl) {
    const field = attrs.ngModel.split('.').slice(-1)[0];

    return ctrl.then(data => {
                 scope.field.meta = data.meta[field];
                 scope.field.form = data.form;

                 activate(scope.field.meta);

                 return data;
               })
               .catch(error => $log.error('selectMultiple.directive error:', error));

    function activate() {

      scope.field.meta.choices = scope.field.meta.choices.map(choice => {
        choice._lower_display_name = choice.display_name.toLowerCase();
        return choice;
      });
    }
  }


}


class selectMultipleController {
  constructor($log) {
    'ngInject';

    this.$log = $log;

    this.selectedItem = null;
    this.searchText = null;
    this.meta = this.meta || {};
    this.form = this.form || {};
    this.model = this.model || [];
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
