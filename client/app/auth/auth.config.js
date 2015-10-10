export default function($httpProvider) {
  'ngInject';

  $httpProvider.interceptors.push(injectInterceptor);
}

function injectInterceptor($rootScope, $q, AUTH_EVENTS) {
  'ngInject';
  return {responseError};

  function responseError(response) {
    $rootScope.$broadcast({
      401: AUTH_EVENTS.notAuthenticated,
      403: AUTH_EVENTS.notAuthorized
    }[response.status], response);
    return $q.reject(response);

  }
}
