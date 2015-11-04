(function() {
  'use strict';

  // list
  angular
    .module('app.pubmed')
    .controller('pubmedListController', pubmedListController);

  /** @ngInject **/
  function pubmedListController($log, PubmedData, $auth, PERMISSION) {
    var vm = this;
    vm.isAuthenticated = $auth.isAuthenticated;
    vm.canAddPubmed = $auth.can.bind(null, PERMISSION.pubmed.add);
    vm.loading = true;
    vm.pubmedEntries = PubmedData.list();
    activate();

    ////////////////

    function activate() {
      vm.pubmedEntries
        .then(function(response) {
          vm.pubmedEntries = response;
          return response;
        })
        .finally(function() {
          vm.loading = false;
        });
    }
  }

})();

