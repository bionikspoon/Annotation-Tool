(function() {
  'use strict';

  angular
    .module('app.auth')
    .factory('$authRunProxy', $authRunProxy);

  /** @ngInject **/
  function $authRunProxy($auth) {
    return $auth;
  }

})();
