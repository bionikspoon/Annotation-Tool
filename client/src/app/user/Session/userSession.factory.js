(function() {
  'use strict';

  angular
    .module('app.user')
    .factory('Session', Session);

  /** @ngInject **/
  function Session($log, $rootScope, AUTH_EVENTS) {
    $rootScope.$on(AUTH_EVENTS.tokenRemove, function() {
      $log.debug('userSession.factory AUTH_EVENTS.tokenRemove:', AUTH_EVENTS.tokenRemove);
    });
    $rootScope.$on(AUTH_EVENTS.tokenSet, function() {
      $log.debug('userSession.factory AUTH_EVENTS.tokenSet:', AUTH_EVENTS.tokenSet);
    });
    var service = {
      functionName: functionName
    };
    return service;

    ////////////////

    function functionName() {
    }
  }

})();

