(function() {
  'use strict';

  angular
    .module('app.auth')
    .constant('AUTH_EVENTS', {
      tokenSet:    'auth-token-set',
      tokenRemove: 'auth-token-remove'
    });

})();
