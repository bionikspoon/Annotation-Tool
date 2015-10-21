(function() {
  'use strict';

  angular
    .module('app.core')
    .config(restangularProviderConfig);

  function pubmedOptionsInterceptor(data, operation, what) {
    if(operation !== 'options' || what !== 'pubmed') {
      return data;
    } else {
      Object.keys(data.actions.POST)
            .forEach(function(key) {
              data.actions.POST[key].name = key;
            });
    }
  }

  /** @ngInject **/
  function restangularProviderConfig(RestangularProvider) {
    RestangularProvider.setBaseUrl('/api');
    RestangularProvider.setRestangularFields({
      selfLink: 'url'
    });
    RestangularProvider.addResponseInterceptor(pubmedOptionsInterceptor);
    RestangularProvider.setRequestSuffix('/');

  }
})();
