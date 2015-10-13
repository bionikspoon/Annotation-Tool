function selectMultipleDirective($log) {
  'ngInject';

  const directive = {
    restrict: 'E',
    templateUrl: 'app/controls/selectMultiple/selectMultiple.html',
    controller: selectMultipleController,
    controllerAs: 'field',
    bindToController: true,
    scope: {model: '=ngModel'},
    require: ['^appFormMeta', 'ngModel'],
    link: link
  };
  return directive;

  function link(scope, element, attrs, [ctrl, ngModel]) {
    const field = attrs.ngModel.split('.').slice(-1)[0];

    return ctrl
      .then(data => {
        scope.field.meta = data.meta[field];
        scope.field.form = data.form;
        scope.field.ngModel = ngModel;

        activate(scope.field.meta);

        return data;
      })
      .catch(error => $log.error('selectMultiple.directive error:', error));

    function activate() {
      scope.field._choices = new Map();
      scope.field.meta.choices.forEach(choice => {
        choice._lower_display_name = choice.display_name.toLowerCase();
        scope.field._choices.set(choice.value, choice);
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
    this.modelOptions = {};

  }

  appendModel(choice) {
    return choice.value;
  }


  activate() {
  }


  querySearch(query) {
    const selected = this.model;
    const results = query ? [...this._choices.values()]
      .filter(this.filterFactoryExcludeSelected(selected))
      .filter(this.filterFactoryLowercase(query)) : [];
    return results;
  }

  filterFactoryExcludeSelected(selected) {
    this.$log.debug('selectMultiple.directive selected:', selected);
    this.$log.debug('selectMultiple.directive this.filterFactoryExcludeSelected.cache:',
      this.filterFactoryExcludeSelected.cache);

    return choice => selected.indexOf(choice.value) === -1;
  }

  filterFactoryLowercase(query) {
    const lowercaseQuery = angular.lowercase(query);
    return choice => choice._lower_display_name.indexOf(lowercaseQuery) !== -1;
  }


  getChipDisplayName(chip) {
    if(this._choices) {
      return this._choices.get(chip).display_name;
    }
  }

}

export default selectMultipleDirective;
