(function() {
  'use strict';

  angular
    .module('app.auth')
    .run(verifyAuthToken)
    .run(authRouteConfig);

  /** @ngInject **/
  function verifyAuthToken($authRunProxy, $log, $q,Toast) {
    if($authRunProxy.isAuthenticated()) {
      $authRunProxy
        .verify()
        .then(Toast.resolve.success('Signed in'))
        .catch(function(error) {
          $log.error('auth.run error:', error);
          return $q.reject(error);
        });
    }
  }

  /** @ngInject **/
  function authRouteConfig($rootScope, $state, $authRunProxy, AUTH_REDIRECT) {
    $rootScope.$on("$stateChangeStart", restrictRoutes);

    function restrictRoutes(event, toState, toParams) {
      // Guard, no restrictions.
      if(!angular.isDefined(toState.data)) {return;}

      var isAuthenticated = $authRunProxy.isAuthenticated();
      var permission = toState.data.permission;
      var authenticate = toState.data.authenticate;
      redirectToLogin = redirectToLogin.bind(null, event, toState, toParams);

      // Requires is authenticated
      if(authenticate === true && !isAuthenticated) {
        return redirectToLogin();
      }

      // Requires not authenticated
      if(authenticate === false && isAuthenticated) {
        return event.preventDefault();
      }

      // Requires permission
      if(angular.isDefined(permission) && !$authRunProxy.can(permission)) {
        return event.preventDefault();
      }

    }

    function redirectToLogin(event, toState, toParams) {
      var next = {
        next: {
          name:   toState.name,
          params: toParams
        }
      };
      $state.go(AUTH_REDIRECT.postLogin, next);
      return event.preventDefault();
    }
  }

})();
