(function() {
  'use strict';

  // form
  angular
    .module('app.pubmed')
    .controller('pubmedFormController', pubmedFormController);

  /** @ngInject **/
  function pubmedFormController(Restangular, $log) {
    var vm = this;

    vm.meta = Restangular.all('pubmed').options();

    activate();

    ////////////////

    function activate() {

      vm.meta.then(function(options) {
        vm.meta = options.actions.POST;
        return options;
      });
    }
  }

})();

