(function() {
  'use strict';

  angular
    .module('app.user')
    .factory('Session', Session);

  /** @ngInject **/
  function Session($http, $log, $rootScope, $timeout, $q, AUTH_EVENTS, SatellizerStorage) {
    var userKey = 'anno_user';

    $rootScope.$on(AUTH_EVENTS.tokenSet, requestGet);
    $rootScope.$on(AUTH_EVENTS.tokenRemove, destroy);

    var service = {};
    Object.defineProperty(service, 'user', {
      get: getUser,
      set: setUser
    });
    return service;

    ////////////////
    function getUser() {
      return JSON.parse(SatellizerStorage.get(userKey));
    }

    function setUser(user) {
      $timeout(SatellizerStorage.set(userKey, JSON.stringify(user)));
    }

    function removeUser() {
      SatellizerStorage.remove(userKey);
    }

    function create(user) {
      service.user = user;

    }

    function destroy() {
      removeUser();
    }

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

