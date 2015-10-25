(function() {
  'use strict';

  // form
  angular
    .module('app.pubmed')
    .controller('pubmedFormController', pubmedFormController);

  /** @ngInject **/
  function pubmedFormController(Restangular, $q) {
    var vm = this;

    vm.meta = pubmedOptions();

    activate();

    ////////////////

    function activate() {
    }

    function pubmedOptions() {
      var deferred = $q.defer();
      Restangular
        .all('pubmed')
        .options()
        .then(function(data) {
          deferred.resolve(data.actions.POST);
        })
        .catch(function(error) {
          deferred.reject(error);
        });
      return deferred.promise;
    }
  }

})();

