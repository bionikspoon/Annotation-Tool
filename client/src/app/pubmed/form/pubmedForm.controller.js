(function() {
  'use strict';

  // form
  angular
    .module('app.pubmed')
    .controller('pubmedFormController', pubmedFormController);

  /** @ngInject **/
  function pubmedFormController() {
    var vm = this;
    vm.title = 'pubmedFormController';

    activate();

    ////////////////

    function activate() {

    }
  }

})();

