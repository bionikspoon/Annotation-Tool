(function() {
  'use strict';

  // form
  angular
    .module('app.pubmed')
    .controller('pubmedFormController', pubmedFormController);

  /** @ngInject **/
  function pubmedFormController($state, $q, PubmedData, Toast) {
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
        .then(Toast.resolve.success('Pubmed entry saved.'))
        .then(function(response) {
          $state.go('pubmed.list');
          return response;
        })
        .catch(Toast.reject.error('Pubmed entry could not be saved.'));
    }
  }

})();

