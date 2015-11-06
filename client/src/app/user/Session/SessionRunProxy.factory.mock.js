(function() {
  'use strict';

  angular
    .module('app.user')
    .config(function($provide) {
      $provide.factory('SessionRunProxy', mockSessionRunProxy);
    });

  /** @ngInject **/
  function mockSessionRunProxy() {return {};}

})();
