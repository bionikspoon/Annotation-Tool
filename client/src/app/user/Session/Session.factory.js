(function() {
  'use strict';

  angular
    .module('app.user')
    .factory('Session', Session);

  /** @ngInject **/
  function Session($http, $log, $rootScope, $q, AUTH_EVENTS, UserStorage) {
    var self = this;

    $rootScope.$on(AUTH_EVENTS.tokenSet, requestGet);
    $rootScope.$on(AUTH_EVENTS.tokenRemove, destroy);

    Object.defineProperty(self, 'user', {
      get: UserStorage.get,
      set: UserStorage.set
    });

    return self;

    ////////////////

    function create(user) {self.user = user;}

    function destroy() {UserStorage.remove();}

    function requestGet() {
      return $http
        .get('/api/auth/profile')
        .then(function(results) {
          var user = {
            id:          results.data.id,
            permissions: results.data.get_all_permissions,
            email:       results.data.email,
            groups:      results.data.groups,
            name:        results.data.name,
            username:    results.data.username
          };
          //$log.debug('$http.requestGet results:', results);
          create(user);
          return results;
        })
        .catch(function(error) {
          $log.error('Session.factory error:', error);
          return $q.reject(error);
        });
    }
  }

})();


