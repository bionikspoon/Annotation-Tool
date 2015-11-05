(function() {
  'use strict';

  angular
    .module('app.user')
    .service('UserData', UserData);

  /** @ngInject **/
  function UserData($http, $log, $q, AUTH_ENDPOINTS) {
    var profileEndpoint = AUTH_ENDPOINTS.prefix + AUTH_ENDPOINTS.profile;

    this.get = get;

    ////////////////

    function get() {
      var deferred = $q.defer();

      $http
        .get(profileEndpoint)
        .then(function(results) {
          var user = {
            id:          results.data.id,
            permissions: results.data.get_all_permissions,
            email:       results.data.email,
            groups:      results.data.groups,
            name:        results.data.name,
            username:    results.data.username
          };
          deferred.resolve(user);
        })
        .catch(function(error) {
          $log.error('UserData.service error:', error);
          deferred.reject(error);
        });

      return deferred.promise;

    }
  }

})();
