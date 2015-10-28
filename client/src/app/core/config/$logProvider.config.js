(function() {
  'use strict';

  angular
    .module('app.core')
    .config($logProviderConfig);

  /** @ngInject **/
  function $logProviderConfig($logProvider) {
    $logProvider.debugEnabled(true);
  }
})();
