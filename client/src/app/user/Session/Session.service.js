(function() {
  'use strict';

  angular
    .module('app.user')
    .service('Session', Session);

  /** @ngInject **/
  function Session($rootScope, $q, AUTH_EVENTS, UserData, UserStorage) {
    var self = this;

    self.create = create;
    self.destroy = destroy;
    self.init = init;

    $rootScope.$on(AUTH_EVENTS.tokenSet, self.init);
    $rootScope.$on(AUTH_EVENTS.tokenRemove, self.destroy);

    Object.defineProperty(self, 'user', {
      get: UserStorage.get,
      set: UserStorage.set
    });

    ////////////////

    function create(user) {
      self.user = user;
    }

    function destroy() {
      UserStorage.remove();
    }

    function init() {
      return UserData
        .get()
        .then(function(user) {
          return self.create(user);
        })
        .catch(function(error) {
          self.destroy();
          return $q.reject(error);
        });
    }
  }

})();
