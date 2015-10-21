(function() {
  'use strict';

  // list
  angular
    .module('app.pubmed')
    .controller('pubmedListController', pubmedListController);

  /** @ngInject **/
  function pubmedListController(Restangular, $log) {
    var vm = this;
    vm.title = 'pubmedListController';

    activate();

    ////////////////

    function activate() {
      Restangular.all('pubmed')
                 .getList()
                 .then(function(pubmedEntries) {
                   vm.pubmedEntries = pubmedEntries;
                 })
                 .catch(function(error) {
                   $log.error('pubmedList.controller error:', error);
                 })
                 .finally(function() {
                   vm.loading = false;
                 });
    }
  }

})();

