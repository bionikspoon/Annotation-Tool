(function() {
  'use strict';

  angular
    .module('app.auth')
    .config(/** @ngInject **/function($provide) {
      $provide.decorator('$auth', $authDecorator);
    });

  /** @ngInject **/
  function $authDecorator($delegate, $injector) {

    $delegate.verify = verify;
    $delegate.can = can;

    return $delegate;

    ////////////////

    function verify(opts) {
      var local = $injector.get('SatellizerLocal');

      return local.verify(opts);
    }

    function can(accessPermission) {
      var Session = $injector.get('Session');
      var user = Session.user;

      // Guard, missing Session.
      if(!user || !angular.isArray(user.permissions)) {return false;}

      return user.permissions.indexOf(accessPermission) !== -1;
    }
  }
})();
