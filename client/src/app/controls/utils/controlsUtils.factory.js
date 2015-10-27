(function() {
  'use strict';

  angular
    .module('app.controls')
    .factory('controlsUtils', controlsUtils);

  /** @ngInject **/
  function controlsUtils() {
    var service = {
      factoryFilterExcludeSelected: factoryFilterExcludeSelected,
      factoryFilterLowercase:       factoryFilterLowercase,
      prepareChoices:               prepareChoices
    };
    return service;

    ////////////////

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

