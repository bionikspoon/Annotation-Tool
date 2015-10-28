(function() {
  'use strict';

  angular
    .module('app.auth')
    .config(satellizerDecorator);

  /** @ngInject **/
  function satellizerDecorator($provide) {
    $provide.decorator('SatellizerStorage', storageDecorator);
  }

  /** @ngInject **/
  function storageDecorator($delegate, $rootScope, SatellizerConfig, AUTH_EVENTS) {
    var set = $delegate.set;
    var remove = $delegate.remove;
    var tokenName = getTokenName(SatellizerConfig);

    $delegate.set = function(key, value) {
      if(key === tokenName) {
        $rootScope.$broadcast(AUTH_EVENTS.tokenSet);
      }
      return set.call(this, key, value);
    };
    $delegate.remove = function(key) {
      if(key === tokenName) {
        $rootScope.$broadcast(AUTH_EVENTS.tokenRemove);
      }
      return remove.call(this, key);
    };

    return $delegate;
  }

  function getTokenName(config) {
    return config.tokenPrefix ? [
      config.tokenPrefix,
      config.tokenName
    ].join('_') : config.tokenName;
  }
})();
