(function() {
  'use strict';

  angular
    .module('app.user')
    .run(userRun);

  /** @ngInject **/
  function userRun(Session) {}

})();
