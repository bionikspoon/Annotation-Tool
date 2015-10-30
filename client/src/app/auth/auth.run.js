(function() {
  'use strict';

  angular
    .module('app.auth')
    .run(authRun);

  /** @ngInject **/
  function authRun($auth, $log, $q) {
    if($auth.isAuthenticated()) {
      $auth.verify()
           .then(function(response) {
             $log.debug('auth.run response:', response);
             return response;
           })
           .catch(function(error) {
             $log.error('auth.run error:', error);
             return $q.reject(error);
           });
    }
  }

})();
