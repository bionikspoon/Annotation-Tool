(function() {
  'use strict';

  // form
  angular
    .module('app.pubmed')
    .controller('pubmedFormController', pubmedFormController);

  /** @ngInject **/
  function pubmedFormController($anchorScroll, $location, $log, $scope, $state, $timeout, $q, PubmedData, Toast) {
    var vm = this;

    vm.meta = PubmedData.options();
    vm.loading = true;
    vm.pubmedRelated = [];
    vm.entry = $state.params.id ? PubmedData.get($state.params.id) : PubmedData.init();

    vm.submit = submit;
    vm.scrollTo = scrollTo;

    $scope.$watch('vm.entry.pubmed_id', getRelatedEntries);

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

    function scrollTo(anchor) {
      var current = $location.hash();
      $location.hash(anchor);
      $anchorScroll();
      $location.hash(current);
    }

    ////////////////

    function getRelatedEntries(value) {
      value = value || vm.entry.pubmed_id;

      // Guard, undefined value
      if(!angular.isDefined(value)) {return undefined;}

      // Guard, invalid pubmed_id
      if(vm.entryForm.pubmed_id.$invalid) {
        return undefined;
      }

      // Build request payload
      var payload = {pubmed_id: value};
      if(angular.isDefined(vm.entry.id)) {
        payload.id = '-' + vm.entry.id;
      }
      $log.debug('pubmedForm.controller payload:', payload);

      // Get matching entries
      return PubmedData.list(payload)
                       .then(function(response) {
                         vm.pubmedRelated = response;
                         $log.debug('pubmedForm.controller response:', response);
                         return response;
                       });
    }

  }

})();

