(function() {
  'use strict';

  // logout
  angular
    .module('app.auth')
    .controller('authLogoutController', authLogoutController);

  /** @ngInject **/
  function authLogoutController($auth, $log, $state, $q, AUTH_REDIRECT, Toast) {

    activate();

    ////////////////

    function activate() {
      $auth.logout()
           .then(Toast.resolve.info('Signed out'))
           .then(function(response) {
             $state.go(AUTH_REDIRECT.postLogout);
             return response;
           })
           .catch(Toast.reject.error('Log out failed.'))
           .catch(function(error) {
             $log.error('authLogout.controller error:', error);
             return $q.reject(error);
           });
    }
  }

})();

