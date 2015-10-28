(function() {
  'use strict';

  // logout
  angular
    .module('app.auth')
    .controller('authLogoutController', authLogoutController);

  /** @ngInject **/
  function authLogoutController($auth) {
    var vm = this;
    vm.title = 'authLogoutController';

    activate();

    ////////////////

    function activate() {
      $auth.logout();
    }
  }

})();

