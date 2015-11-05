(function() {
  'use strict';

  angular
    .module('app.auth')
    .run(runSatellizerConfig);

  /** @ngInject **/
  function runSatellizerConfig(SatellizerConfig, AUTH_ENDPOINTS) {
    SatellizerConfig.refreshUrl = AUTH_ENDPOINTS.refresh;
    SatellizerConfig.verifyUrl = AUTH_ENDPOINTS.verify;
  }

})();
