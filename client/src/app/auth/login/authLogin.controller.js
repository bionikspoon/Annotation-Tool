(function() {
  'use strict';

  // login
  angular
    .module('app.auth')
    .controller('authLoginController', authLoginController);

  /** @ngInject **/
  function authLoginController($log, $state, $q, $auth, REDIRECT, Toast) {
    var vm = this;
    var next;
    vm.login = login;

    activate();

    ////////////////

    function activate() {
      var fallbackNext = {
        name:   REDIRECT.postLogin,
        params: {}
      };

      next = $state.params.next || fallbackNext;
      next = next.name === 'auth.logout' ? fallbackNext : next;
    }

    function login(credentials) {
      return $auth.login(credentials)
                  .then(Toast.resolve.success('Signed in'))
                  .then(function(response) {
                    $state.go(next.name, next.params);
                    return response;
                  })
                  .catch(Toast.reject.error('Authentication failed.'))
                  .catch(function(error) {
                    $log.error('authLogin.controller error:', error);
                    return $q.reject(error);
                  });
    }
  }

})();

