(function() {
  'use strict';

  angular
    .module('app.main')
    .controller('MainController', MainController);

  /** @ngInject */
  function MainController($log, $scope, $auth, AUTH_EVENTS, Session) {
    var vm = this; // jshint ignore:line

    //$scope.$on(AUTH_EVENTS.login, createSession);
    //$scope.$on(AUTH_EVENTS.verify, createSession);
    //$scope.$on(AUTH_EVENTS.refresh, createSession);
    //createSession();

    activate();

    function activate() {
    }

    //function createSession() {
    //  if(!$auth.isAuthenticated()) {
    //    return $log.error('Not authenticated. main.controller arguments:', arguments);
    //  }
    //  if(!angular.isDefined(arguments[0])) {
    //    return $log.debug('main.controller arguments:', arguments);
    //
    //  }
    //  $log.debug('main.controller Session:', Session);
    //  return $log.debug('main.controller arguments, arguments[0].name:', arguments, arguments[0].name);
    //
    //}

  }

})();
