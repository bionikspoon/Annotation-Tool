(function() {
  'use strict';

  // logout
  angular
    .module('app.auth')
    .controller('authLogoutController', authLogoutController);

  /** @ngInject **/
  function authLogoutController($auth, $state, REDIRECT) {
    //noinspection JSUnusedLocalSymbols
    var vm = this; // jshint ignore:line

    activate();

    ////////////////

    function activate() {
      $auth.logout()
           .then(function(response) {
             $state.go(REDIRECT.postLogout);
             return response;
           });
    }
  }

})();

