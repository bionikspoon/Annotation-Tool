(function() {
  'use strict';

  angular
    .module('app.controls')
    .factory('controlsUtils', controlsUtils);

  /** @ngInject **/
  function controlsUtils($q, $log) {
    var service = {
      factoryFilterExcludeSelected: factoryFilterExcludeSelected,
      factoryFilterLowercase:       factoryFilterLowercase,
      prepareChoices:               prepareChoices,
      fieldMeta:                    fieldMeta,
      fieldForm:                    fieldForm
    };
    return service;

    ////////////////
    function fieldMeta() {
      var self = this;

      return $q.when(self.formMeta.meta)
               .then(function(meta) {
                 self.scope.vm.meta = meta[self.field];
                 return meta[self.field];
               })
               .catch(function(error) {
                 $log.error('fieldMeta controlsUtils.factory error:', error);
                 return $q.reject(error);
               });
    }

    function fieldForm() {
      var self = this;

      return $q.when(self.formMeta.form)
               .then(function(form) {
                 self.scope.vm.form = form;
                 return form;
               })
               .catch(function(error) {
                 $log.error('fieldForm controlsGenericInput.directive error:', error);
                 return $q.reject(error);
               });
    }

    function factoryFilterExcludeSelected(selected) {
      return function(choice) { return selected.indexOf(choice.value) === -1; };
    }

    function factoryFilterLowercase(query) {
      var lowercaseQuery = angular.lowercase(query);
      return function(choice) { return choice._lower_display_name.indexOf(lowercaseQuery) !== -1; };
    }

    function prepareChoices(choices) {
      var _choices = {};
      angular.forEach(choices, function(choice) {
        choice._lower_display_name = choice.display_name.toLowerCase();
        _choices[choice.value] = choice;
      });
      return _choices;
    }
  }

})();

