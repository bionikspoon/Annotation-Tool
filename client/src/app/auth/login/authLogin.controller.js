(function() {
  'use strict';

  // login
  angular
    .module('app.auth')
    .controller('authLoginController', authLoginController);

  /** @ngInject **/
  function authLoginController($log, $state, $q, $auth) {
    var vm = this;
    vm.login = login;

    ////////////////

    function login(credentials) {
      return $auth.login(credentials)
                  .then(function(response) {
                    $state.go('pubmed.list');
                    return response;
                  })
                  .catch(function(error) {
                    $log.error('authLogin.controller error:', error);
                    return $q.reject(error);
                  });
    }
  }

})();

