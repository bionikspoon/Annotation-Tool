(function() {
  'use strict';

  angular
    .module('app.core')
    .config(restangularProviderConfig);

  /** @ngInject **/
  function restangularProviderConfig(RestangularProvider) {
    RestangularProvider.setBaseUrl('/api');
    RestangularProvider.setRestangularFields({
      selfLink: 'url'
    });
    RestangularProvider.setRequestSuffix('/');

    RestangularProvider.addResponseInterceptor(optionsInterceptor);

    function optionsInterceptor(data, operation) {
      if(operation !== 'options') {
        return data;
      }

      angular.forEach(data.actions.POST, function(option, key) {option.name = key;});
      return data;
    }
  }

})();
