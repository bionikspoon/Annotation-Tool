(function() {
  'use strict';

  angular
    .module('app.auth')
    .factory('AuthLoginData', AuthLoginData);

  /** @ngInject **/
  function AuthLoginData($log, $q, Restangular) {
    var service = {
      options: options
    };
    return service;

    ////////////////

    function options() {
      var deferred = $q.defer();
      Restangular
        .all('auth')
        .all('login')
        .options()
        .then(function(data) {
          data.actions.POST.password.type = 'password';
          $log.debug('AuthLoginData.factory data:', data);
          return deferred.resolve(data.actions.POST);
        })
        .catch(function(error) {
          $log.error('AuthLoginData.factory error:', error);
          return deferred.reject(error);
        });

      return deferred.promise;
    }
  }

})();
