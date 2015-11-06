(function() {
  'use strict';

  angular
    .module('app.auth')
    .constant('AUTH_EVENT', {
      tokenSet:    'auth-token-set',
      tokenRemove: 'auth-token-remove',
      login:       'auth-login',
      refresh:     'auth-refresh',
      verify:      'auth-verify'
    });

})();
