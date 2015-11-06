(function() {
  'use strict';

  // login
  angular
    .module('app.auth')
    .controller('authLoginController', authLoginController);

  /** @ngInject **/
  function authLoginController($log, $state, $q, $auth) {
    var vm = this;
    var next;
    vm.login = login;

    activate();

    ////////////////

    function activate() {
      next = $state.params.next || {
          name:   'pubmed.list',
          params: {}
        };
    }

    function login(credentials) {
      return $auth.login(credentials)
                  .then(function(response) {
                    $state.go(next.name, next.params);
                    return response;
                  })
                  .catch(function(error) {
                    $log.error('authLogin.controller error:', error);
                    return $q.reject(error);
                  });
    }
  }

})();

