export default function($httpProvider) {
  'ngInject';

  // TODO enable this.
  $httpProvider.interceptors.push(injectInterceptor);
}

function injectInterceptor($rootScope, $q, AUTH_EVENTS, Session) {
  'ngInject';
  return {
    responseError,
    request
  };

  function responseError(response) {
    $rootScope.$broadcast({
      401: AUTH_EVENTS.notAuthenticated,
      403: AUTH_EVENTS.notAuthorized
    }[response.status], response);
    return $q.reject(response);
  }

  function request(config) {
    if(!!Session.token) {
      config.headers.Authorization = 'JWT ' + Session.token;
    }
    return config;
  }
}
