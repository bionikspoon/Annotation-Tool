(function() {
  'use strict';

  angular
    .module('app.user')
    .factory('SessionRunProxy', SessionRunProxy);

  /** @ngInject **/
  function SessionRunProxy(Session) {
    return Session;
  }

})();
