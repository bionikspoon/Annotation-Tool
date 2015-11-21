(function() {
  'use strict';

  angular
    .module('app.auth')
    .config($authProviderConfig);

  /** @ngInject **/
  function $authProviderConfig($authProvider, AUTH_ENDPOINT) {
    $authProvider.baseUrl = AUTH_ENDPOINT.prefix;
    $authProvider.loginUrl = AUTH_ENDPOINT.login;
    $authProvider.signupUrl = AUTH_ENDPOINT.signup;
    $authProvider.tokenPrefix = 'anno';

  }
})();
