(function() {
  'use strict';

  angular
    .module('app.user')
    .factory('Session', Session);

  /** @ngInject **/
  function Session($rootScope, $q, AUTH_EVENTS, UserData, UserStorage) {
    var service = {
      create:  create,
      destroy: destroy,
      init:    init,
      can:     can
    };

    $rootScope.$on(AUTH_EVENTS.tokenSet, service.init);
    $rootScope.$on(AUTH_EVENTS.tokenRemove, service.destroy);
    Object.defineProperty(service, 'user', {
      get: UserStorage.get,
      set: UserStorage.set
    });
    return service;

    ////////////////

    function create(user) {
      service.user = user;

    }

    function destroy() {
      UserStorage.remove();

    }

    function init() {
      return UserData
        .get()
        .then(function(user) {
          return service.create(user);
        })
        .catch(function(error) {
          service.destroy();
          return $q.reject(error);
        });

    }

    function can(permission) {
      var user = service.user;
      if(!user || !angular.isArray(user.permissions)) {
        return false;
      }

      return user.permissions.indexOf(permission) !== -1;
    }
  }

})();
