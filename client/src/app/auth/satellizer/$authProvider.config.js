(function() {
  'use strict';

  angular
    .module('app.auth')
    .config($authProviderConfig);

  /** @ngInject **/
  function $authProviderConfig($authProvider, AUTH_ENDPOINTS) {
    $authProvider.baseUrl = AUTH_ENDPOINTS.prefix;
    $authProvider.loginUrl = AUTH_ENDPOINTS.login;
    $authProvider.signupUrl = AUTH_ENDPOINTS.signup;
    $authProvider.tokenPrefix = 'anno';

  }
})();
