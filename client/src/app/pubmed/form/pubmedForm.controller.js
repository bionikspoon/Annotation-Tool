(function() {
  'use strict';

  angular
    .module('app.pubmed')
    .controller('PubmedFormController', PubmedFormController);

  /** @ngInject **/
  function PubmedFormController() {
    var vm = this;
    vm.title = 'PubmedFormController';

    activate();

    ////////////////

    function activate() {
    }
  }

})();

