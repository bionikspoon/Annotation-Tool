export default function($log, $rootScope, AUTH_EVENTS, AuthService) {
  'ngInject';

  $rootScope.$on('$stateChangeStart', (event, next) => {
    if(angular.isDefined(next.data)) {
      const authorizedRoles = next.data.authorizedRoles;
      if(!AuthService.isAuthorized(authorizedRoles)) {
        event.preventDefault();
        // TODO handle redirection

        if(AuthService.isAuthenticated()) {
          $rootScope.$broadcast(AUTH_EVENTS.notAuthorized);
        } else {
          $rootScope.$broadcast(AUTH_EVENTS.notAuthenticated);
        }

      }
    }
  });
}
