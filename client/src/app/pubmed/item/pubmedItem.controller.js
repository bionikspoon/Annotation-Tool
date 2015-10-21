(function() {
  'use strict';

  // item
  angular
    .module('app.pubmed')
    .controller('pubmedItemController', pubmedItemController);

  /** @ngInject **/
  function pubmedItemController() {
    var vm = this;
    vm.title = 'pubmedItemController';

    activate();

    ////////////////

    function activate() {

    }
  }

})();

