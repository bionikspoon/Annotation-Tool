(function() {
  'use strict';

  // login
  angular
    .module('app.auth')
    .controller('authLoginController', authLoginController);

  /** @ngInject **/
  function authLoginController() {
    var vm = this;
    vm.title = 'authLoginController';

    activate();

    ////////////////

    function activate() {

    }
  }

})();

