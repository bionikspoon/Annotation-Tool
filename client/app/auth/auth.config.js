export default function($httpProvider) {
  'ngInject';

  $httpProvider.interceptors.push(injectInterceptor);
}

function injectInterceptor($rootScope, $q, $log, AUTH_EVENTS, Session) {
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
      $log.debug('auth.config config, Session:', config, Session);
    }
    return config;
  }
}
