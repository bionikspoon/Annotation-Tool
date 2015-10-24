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

  }

})();
