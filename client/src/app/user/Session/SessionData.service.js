(function() {
  'use strict';

  angular
    .module('app.user')
    .service('SessionData', SessionData);

  /** @ngInject **/
  function SessionData($http, $log, $q) {
    var profileUrl = '/api/auth/profile';

    this.get = get;

    ////////////////

    function get() {
      var deferred = $q.defer();

      $http
        .get(profileUrl)
        .then(function(results) {
          var user = {
            id:          results.data.id,
            permissions: results.data.get_all_permissions,
            email:       results.data.email,
            groups:      results.data.groups,
            name:        results.data.name,
            username:    results.data.username
          };
          return deferred.resolve(user);
        })
        .catch(function(error) {
          $log.error('SessionData.service error:', error);
          return deferred.reject(error);
        });

      return deferred.promise;

    }
  }

})();
