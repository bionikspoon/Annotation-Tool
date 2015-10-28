(function() {
  'use strict';

  angular
    .module('app.auth')
    .config($authProviderConfig);

  /** @ngInject **/
  function $authProviderConfig($authProvider) {
    $authProvider.baseUrl = '/api/';
    $authProvider.loginUrl = '/auth/login/';
    $authProvider.signupUrl = '/auth/signup/';
    $authProvider.tokenPrefix = 'anno';

  }
})();
