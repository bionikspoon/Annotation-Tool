(function() {
  'use strict';

  // login
  angular
    .module('app.auth')
    .controller('authLoginController', authLoginController);

  /** @ngInject **/
  function authLoginController($log, $q, $auth, Session) {
    var vm = this;
    vm.title = 'authLoginController';
    vm.login = login;
    activate();

    ////////////////

    function activate() {
    }

    function login(credentials) {
      $log.debug('authLogin.controller credentials:', credentials);
      $auth.login(credentials)
           .then(function(response) {
             $log.debug('authLogin.controller response:', response);
             $log.debug('authLogin.controller $auth.getPayload():', $auth.getPayload());
             return response;
           })
           .catch(function(error) {
             $log.error('authLogin.controller error:', error);
             return $q.reject(error);
           });
    }
  }

})();

