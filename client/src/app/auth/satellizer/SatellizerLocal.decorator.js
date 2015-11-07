/* global escape, window*/
(function() {
  'use strict';

  angular
    .module('app.auth')
    .config(/** @ngInject **/function($provide) {
      $provide.decorator('SatellizerLocal', SatellizerLocalDecorator);
    });

  /** @ngInject **/
  function SatellizerLocalDecorator($delegate, $injector, $http, $timeout, $q, AUTH_EVENT, $log) {
    var _login = $delegate.login;

    $delegate.login = login;
    $delegate.refresh = refresh;
    $delegate.verify = verify;

    return $delegate;

    ////////////////

    function login(user, opts) {
      return _login.call(this, user, opts)
                   .then(thenTriggerRefresh)
                   .then(thenBroadcast(AUTH_EVENT.login));
    }

    function refresh(timeout, opts) {
      opts = opts || {};
      opts.url = getRefreshUrl();
      opts.method = opts.method || 'POST';

      return $timeout(_refresh, timeout);

      function _refresh() {
        var shared = $injector.get('SatellizerShared');

        // Guard
        var token = shared.getToken();
        if(token === null) {return $q.reject('Token cannot be null');}

        opts.data = {token: token};
        return $http(opts)
          .then(thenSetToken)
          .then(thenTriggerRefresh)
          .then(thenBroadcast(AUTH_EVENT.refresh));
      }

    }

    function verify(opts) {
      var shared = $injector.get('SatellizerShared');

      // Guard
      var token = shared.getToken();
      if(token === null) {return $q.reject('Token cannot be null');}

      opts = opts || {};
      opts.url = getVerifyUrl();
      opts.data = {token: token};
      opts.method = opts.method || 'POST';

      return $http(opts)
        .then(thenSetToken)
        .then(thenTriggerRefresh)
        .then(thenBroadcast(AUTH_EVENT.verify));
    }

    ////////////////

    function thenTriggerRefresh(response) {
      var payload = getPayload(response.data.token);

      if(!angular.isDefined(payload)) {
        return $q.reject(response);
      }

      var exp = payload.exp;
      var delta = exp * 1000 - Math.round(new Date().getTime()) - 1000;

      $delegate.refresh.call($delegate, delta);
      return response;

    }

    function thenSetToken(response) {
      var shared = $injector.get('SatellizerShared');

      shared.setToken(response);
      return response;
    }

    function thenBroadcast(event) {
      var $rootScope = $injector.get('$rootScope');

      return function(response) {
        $rootScope.$broadcast(event);
        return response;
      };
    }

    function getRefreshUrl() {
      var config = $injector.get('SatellizerConfig');
      var utils = $injector.get('SatellizerUtils');

      return config.baseUrl ? utils.joinUrl(config.baseUrl, config.refreshUrl) : config.refreshUrl;
    }

    function getVerifyUrl() {
      var config = $injector.get('SatellizerConfig');
      var utils = $injector.get('SatellizerUtils');

      return config.baseUrl ? utils.joinUrl(config.baseUrl, config.verifyUrl) : config.verifyUrl;
    }

    function getPayload(token) {
      if(token && token.split('.').length === 3) {
        try {
          var base64Url = token.split('.')[1];
          var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
          return JSON.parse(decodeURIComponent(escape(window.atob(base64))));
        } catch(e) {
          return undefined;
        }
      }
    }
  }

})();
