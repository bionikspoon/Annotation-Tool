export default class AuthInterceptorService {
  constructor($rootScope, $q, AUTH_EVENTS) {
    'ngInject';
    this.$rootScope = $rootScope;
    this.$q = $q;
    this.AUTH_EVENTS = AUTH_EVENTS;
    const service = {responseError: this.ResponseError};
    return service;

  }

  responseError(response) {
    this.$rootScope.$broadcast({
      401: this.AUTH_EVENTS.notAuthenticated,
      403: this.AUTH_EVENTS.notAuthorized
    }[response.status], response);
    return this.$q.reject(response);
  }
}
