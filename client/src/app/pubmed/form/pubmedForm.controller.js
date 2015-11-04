(function() {
  'use strict';

  // form
  angular
    .module('app.pubmed')
    .controller('pubmedFormController', pubmedFormController);

  /** @ngInject **/
  function pubmedFormController($state, $q, PubmedData) {
    var vm = this;

    vm.meta = PubmedData.options();
    vm.loading = true;
    vm.entry = $state.params.id ? PubmedData.get($state.params.id) : PubmedData.init();
    vm.submit = submit;

    activate();

    ////////////////

    function activate() {

      vm.entry
        .then(function(response) {
          vm.entry = response;
          return response;
        });

      $q.all([
          vm.meta,
          vm.entry
        ])
        .finally(function() {
          vm.loading = false;
        });

    }

    function submit(model) {
      PubmedData
        .save(model)
        .then(function(response) {
          $state.go('pubmed.list');
          return response;
        });
    }
  }

})();

