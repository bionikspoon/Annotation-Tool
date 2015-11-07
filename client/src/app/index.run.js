(function() {
  'use strict';

  angular
    .module('app')
    .run(indexRun);

  /** @ngInject */
  function indexRun($log) {
    $log.debug('\'allo \'allo');
  }

})();
