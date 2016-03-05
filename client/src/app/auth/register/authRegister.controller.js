(function() {
  'use strict';

  // register
  angular
    .module('app.auth')
    .controller('authRegisterController', authRegisterController);

  /** @ngInject **/
  function authRegisterController() {
    var vm = this;
    vm.title = 'authRegisterController';

    activate();

    ////////////////

    function activate() {

    }
  }

})();

