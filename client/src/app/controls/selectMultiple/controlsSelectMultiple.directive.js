(function() {
  'use strict';

  // selectMultiple
  angular
    .module('app.controls')
    .directive('appSelectMultiple', controlsSelectMultipleDirective);

  /** @ngInject **/
  function controlsSelectMultipleDirective($log, $q, controlsUtils) {
    var directive = {
      bindToController: true,
      controller:       controlsSelectMultipleController,
      controllerAs:     'vm',
      link:             link,
      restrict:         'E',
      templateUrl:      'app/controls/selectMultiple/controlsSelectMultiple.html',
      scope:            {model: '=ngModel'},
      require:          [
        '^appFormMeta',
        'ngModel'
      ]
    };
    return directive;

    //noinspection JSUnusedLocalSymbols
    function link(scope, element, attrs, ctrls) {
      var field = attrs.ngModel
                       .split('.')
                       .slice(-1)[0];
      var formMeta = ctrls[0];
      var ngModel = ctrls[1];

      /** @namespace scope.vm */
      scope.vm.meta = fieldMeta();
      scope.vm.form = fieldForm();
      scope.vm._choices = getFieldChoices();
      scope.vm.ngModel = ngModel;

      function fieldMeta() {
        return $q.when(formMeta.meta)
                 .then(function(meta) {
                   scope.vm.meta = meta[field];
                   return meta[field];
                 })
                 .catch(function(error) {
                   $log.error('controlsGenericInput.directive error:', error);
                   return $q.reject(error);
                 });
      }

      function fieldForm() {
        return $q.when(formMeta.form)
                 .then(function(form) {
                   scope.vm.form = form;
                   return form;
                 })
                 .catch(function(error) {
                   $log.error('controlsGenericInput.directive error:', error);
                   return $q.reject(error);
                 });
      }

      function getFieldChoices() {
        var deferred = $q.defer();
        $q.when(scope.vm.meta)
          .then(function(meta) {
            scope.vm._choices = controlsUtils.prepareChoices(meta.choices);
            deferred.resolve(scope.vm._choices);
            return scope.vm._choices;
          })
          .catch(function(error) {
            $log.error('controlsSelectMultiple.directive error:', error);
            deferred.reject(error);
            scope.vm._choices = [];
            return $q.reject(error);
          });

        return deferred.promise;
      }

    }
  }

  /** @ngInject **/
  function controlsSelectMultipleController(_, controlsUtils) {
    var vm = this;
    vm.selectedItem = null;
    vm.searchText = null;
    vm.model = vm.model || [];
    vm.modelOptions = {};
    vm.querySearch = querySearch;
    vm.appendModel = appendModel;
    vm.getChipDisplayName = getChipDisplayName;

    activate();

    ////////////////

    function activate() {}

    function appendModel(choice) {
      return choice.value;
    }

    function querySearch(query) {
      var selected = vm.model;
      return query ? _.valuesIn(vm._choices)
                      .filter(controlsUtils.factoryFilterExcludeSelected(selected))
                      .filter(controlsUtils.factoryFilterLowercase(query)) : [];
    }

    function getChipDisplayName(chip) {
      if(vm._choices) {
        return vm._choices[chip].display_name;
      }
    }
  }

})();

