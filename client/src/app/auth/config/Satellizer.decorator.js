(function() {
  'use strict';

  angular
    .module('app.auth')
    .config(satellizerDecorator);

  /** @ngInject **/
  function satellizerDecorator($provide) {
    $provide.decorator('SatellizerStorage', storageDecorator);
    $provide.decorator('SatellizerLocal', localDecorator);
    $provide.decorator('$auth', $authDecorator);
  }

  /** @ngInject **/
  function storageDecorator($delegate, $rootScope, SatellizerConfig, AUTH_EVENTS) {
    var _set = $delegate.set;
    var _remove = $delegate.remove;
    var tokenName = getTokenName(SatellizerConfig);

    $delegate.set = set;
    $delegate.remove = remove;

    return $delegate;

    function set(key, value) {
      if(key === tokenName) {
        $rootScope.$broadcast(AUTH_EVENTS.tokenSet);
      }
      return _set.call(this, key, value);
    }

    function remove(key) {
      if(key === tokenName) {
        $rootScope.$broadcast(AUTH_EVENTS.tokenRemove);
      }
      return _remove.call(this, key);
    }
  }

  /** @ngInject **/
  function localDecorator($delegate, $http, $rootScope, $timeout, $q, SatellizerShared, SatellizerUtils,
                          SatellizerConfig, AUTH_ENDPOINTS, AUTH_EVENTS) {

    var _login = $delegate.login;
    SatellizerConfig.refreshUrl = AUTH_ENDPOINTS.refresh;
    SatellizerConfig.verifyUrl = AUTH_ENDPOINTS.verify;
    $delegate.login = login;
    $delegate.refresh = refresh;
    $delegate.verify = verify;
    return $delegate;

    function login(user, opts) {
      return _login.call(this, user, opts)
                   .then(triggerRefresh)
                   .then(broadcast(AUTH_EVENTS.login));
    }

    function refresh(timeout, opts) {
      opts = opts || {};
      opts.url = getRefreshUrl(SatellizerConfig, SatellizerUtils);
      opts.method = opts.method || 'POST';

      return $timeout(function() {
        opts.data = {token: SatellizerShared.getToken()};
        return $http(opts);
      }, timeout)
        .then(setToken)
        .then(triggerRefresh)
        .then(broadcast(AUTH_EVENTS.refresh));

    }

    function verify(opts) {
      var token = SatellizerShared.getToken();
      if(token === null) {
        return $q.reject('Token cannot be null');
      }

      opts = opts || {};
      opts.url = getVerifyUrl(SatellizerConfig, SatellizerUtils);
      opts.data = {token: token};
      opts.method = opts.method || 'POST';

      return $http(opts)
        .then(setToken)
        .then(triggerRefresh)
        .then(broadcast(AUTH_EVENTS.verify));
    }

    function triggerRefresh(response) {
      var exp = SatellizerShared.getPayload().exp;
      var delta = exp * 1000 - Math.round(new Date().getTime()) - 1000;
      $delegate.refresh.call($delegate, delta);
      return response;

    }

    function setToken(response) {
      SatellizerShared.setToken(response);
      return response;
    }

    function broadcast(event) {
      return function(response) {
        $rootScope.$broadcast(event);
        return response;
      };
    }

  }

  /** @ngInject **/
  function $authDecorator($delegate, SatellizerLocal) {
    $delegate.verify = verify;
    return $delegate;

    function verify(opts) {
      return SatellizerLocal.verify(opts);
    }

  }

  function getRefreshUrl(config, utils) {
    return config.baseUrl ? utils.joinUrl(config.baseUrl, config.refreshUrl) : config.refreshUrl;
  }

  function getVerifyUrl(config, utils) {
    return config.baseUrl ? utils.joinUrl(config.baseUrl, config.verifyUrl) : config.verifyUrl;
  }

  function getTokenName(config) {
    return config.tokenPrefix ? [
      config.tokenPrefix,
      config.tokenName
    ].join('_') : config.tokenName;
  }
})();
