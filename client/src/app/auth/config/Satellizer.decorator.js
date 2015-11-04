(function() {
  'use strict';

  angular
    .module('app.auth')
    .config(satellizerDecorator)
    .run(runSatellizerConfig);

  /** @ngInject **/
  function satellizerDecorator($provide) {
    $provide.decorator('SatellizerStorage', storageDecorator);
    $provide.decorator('SatellizerLocal', localDecorator);
    $provide.decorator('$auth', $authDecorator);
  }

  /** @ngInject **/
  function runSatellizerConfig(SatellizerConfig, AUTH_ENDPOINTS) {
    SatellizerConfig.refreshUrl = AUTH_ENDPOINTS.refresh;
    SatellizerConfig.verifyUrl = AUTH_ENDPOINTS.verify;
  }

  /** @ngInject **/
  function storageDecorator($delegate, $injector, AUTH_EVENTS) {
    var _set = $delegate.set;
    var _remove = $delegate.remove;
    var tokenName = getTokenName($injector);

    $delegate.set = set;
    $delegate.remove = remove;

    return $delegate;

    ////////////////

    function set(key, value) {
      if(key === tokenName) {
        var $rootScope = $injector.get('$rootScope');
        $rootScope.$broadcast(AUTH_EVENTS.tokenSet);
      }
      return _set.call(this, key, value);
    }

    function remove(key) {
      if(key === tokenName) {
        var $rootScope = $injector.get('$rootScope');
        $rootScope.$broadcast(AUTH_EVENTS.tokenRemove);
      }
      return _remove.call(this, key);
    }
  }

  /** @ngInject **/
  function localDecorator($delegate, $http, $injector, $timeout, $q, AUTH_EVENTS) {
    var _login = $delegate.login;
    var shared = $injector.get('SatellizerShared');

    $delegate.login = login;
    $delegate.refresh = refresh;
    $delegate.verify = verify;

    return $delegate;

    ////////////////

    function login(user, opts) {
      return _login.call(this, user, opts)
                   .then(thenTriggerRefresh)
                   .then(thenBroadcast(AUTH_EVENTS.login));
    }

    function refresh(timeout, opts) {
      opts = opts || {};
      opts.url = getRefreshUrl($injector);
      opts.method = opts.method || 'POST';

      return $timeout(_refresh, timeout)
        .then(thenSetToken)
        .then(thenTriggerRefresh)
        .then(thenBroadcast(AUTH_EVENTS.refresh));

      function _refresh() {
        opts.data = {token: shared.getToken()};
        return $http(opts);
      }

    }

    function verify(opts) {
      var token = shared.getToken();
      // Guard
      if(token === null) {return $q.reject('Token cannot be null');}

      opts = opts || {};
      opts.url = getVerifyUrl($injector);
      opts.data = {token: token};
      opts.method = opts.method || 'POST';

      return $http(opts)
        .then(thenSetToken)
        .then(thenTriggerRefresh)
        .then(thenBroadcast(AUTH_EVENTS.verify));
    }

    ////////////////

    function thenTriggerRefresh(response) {
      var exp = shared.getPayload().exp;
      var delta = exp * 1000 - Math.round(new Date().getTime()) - 1000;

      $delegate.refresh.call($delegate, delta);
      return response;

    }

    function thenSetToken(response) {
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

  }

  /** @ngInject **/
  function $authDecorator($delegate, $injector) {
    var local = $injector.get('SatellizerLocal');
    $delegate.verify = verify;
    $delegate.can = can;

    return $delegate;

    ////////////////

    function verify(opts) {
      return local.verify(opts);
    }

    function can(accessPermission) {
      var Session = $injector.get('Session');
      var user = Session.user;

      // Guard, missing Session.
      if(!user || !angular.isArray(user.permissions)) {return false;}

      return user.permissions.indexOf(accessPermission) !== -1;
    }

  }

  function getRefreshUrl($injector) {
    var config = $injector.get('SatellizerConfig');
    var utils = $injector.get('SatellizerUtils');

    return config.baseUrl ? utils.joinUrl(config.baseUrl, config.refreshUrl) : config.refreshUrl;
  }

  function getVerifyUrl($injector) {
    var config = $injector.get('SatellizerConfig');
    var utils = $injector.get('SatellizerUtils');

    return config.baseUrl ? utils.joinUrl(config.baseUrl, config.verifyUrl) : config.verifyUrl;
  }

  function getTokenName($injector) {
    var config = $injector.get('SatellizerConfig');

    return config.tokenPrefix ? [
      config.tokenPrefix,
      config.tokenName
    ].join('_') : config.tokenName;
  }
})();
