(function() {
  'use strict';

  angular
    .module('app.pubmed')
    .controller('PubmedItemController', PubmedItemController);

  /** @ngInject **/
  function PubmedItemController() {
    var vm = this;
    vm.title = 'PubmedItemController';

    activate();

    ////////////////

    function activate() {

    }
  }

})();

