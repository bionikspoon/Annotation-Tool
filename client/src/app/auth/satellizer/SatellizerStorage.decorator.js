(function() {
  'use strict';

  angular
    .module('app.auth')
    .config(authDecorator);

  /** @ngInject **/
  function authDecorator($provide) {
    $provide.decorator('SatellizerStorage', SatellizerStorageDecorator);
  }

  /** @ngInject **/
  function SatellizerStorageDecorator($delegate, $injector, AUTH_EVENT) {
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
        $rootScope.$broadcast(AUTH_EVENT.tokenSet);
      }
      return _set.call(this, key, value);
    }

    function remove(key) {
      if(key === tokenName) {
        var $rootScope = $injector.get('$rootScope');
        $rootScope.$broadcast(AUTH_EVENT.tokenRemove);
      }
      return _remove.call(this, key);
    }
  }


  function getTokenName($injector) {
    var config = $injector.get('SatellizerConfig');

    return config.tokenPrefix ? [
      config.tokenPrefix,
      config.tokenName
    ].join('_') : config.tokenName;
  }
})();
