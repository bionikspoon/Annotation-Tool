(function() {
  'use strict';

  angular
    .module('app.pubmed')
    .config(restangularProviderConfig);

  /** @ngInject **/
  function restangularProviderConfig(RestangularProvider) {
    RestangularProvider.addResponseInterceptor(pubmedOptionsInterceptor);
  }

  function pubmedOptionsInterceptor(data, operation, what) {
    if(operation !== 'options' || what !== 'pubmed') {
      return data;
    }

    angular.forEach(data.actions.POST, includeFieldName);
    return data;

    //noinspection JSUnusedLocalSymbols
    function includeFieldName(_, key) {
      data.actions.POST[key].name = key;
    }
  }

})();
