(function() {
  'use strict';

  angular
    .module('app.auth')
    .run(runSatellizerConfig);

  /** @ngInject **/
  function runSatellizerConfig(SatellizerConfig, AUTH_ENDPOINT) {
    SatellizerConfig.refreshUrl = AUTH_ENDPOINT.refresh;
    SatellizerConfig.verifyUrl = AUTH_ENDPOINT.verify;
  }

})();
