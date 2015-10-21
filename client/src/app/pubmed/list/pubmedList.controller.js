(function() {
  'use strict';

  angular
    .module('app.pubmed')
    .controller('PubmedListController', PubmedListController);

  /** @ngInject **/
  function PubmedListController($log, Restangular) { // jshint ignore:line
    var vm = this;

    vm.loading = true;
    vm.pubmedEntries = [];

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

