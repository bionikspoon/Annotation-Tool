(function() {
  'use strict';

  angular
    .module('app.user')
    .factory('Session', Session);

  /** @ngInject **/
  function Session($rootScope, $q, AUTH_EVENT, UserData, UserStorage) {
    var service = {
      create:  create,
      destroy: destroy,
      init:    init
    };

    $rootScope.$on(AUTH_EVENT.tokenSet, service.init);
    $rootScope.$on(AUTH_EVENT.tokenRemove, service.destroy);
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
  }

})();
