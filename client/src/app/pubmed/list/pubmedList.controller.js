(function() {
  'use strict';

  // list
  angular
    .module('app.pubmed')
    .controller('pubmedListController', pubmedListController);

  /** @ngInject **/
  function pubmedListController(PubmedData, $auth, PERMISSION, Toast) {
    var vm = this;

    vm.isAuthenticated = $auth.isAuthenticated;

    vm.canAddPubmed = $auth.can.bind(null, PERMISSION.pubmed.pubmed.add);
    vm.canChangePubmed = $auth.can.bind(null, PERMISSION.pubmed.pubmed.change);
    vm.loading = true;
    vm.pubmedEntries = PubmedData.list();

    var title = 'Our secret stigma for purpose is to respect others confidently.';
    var message = 'Remember: shreded pork butt tastes best when pressed in an ice blender enameled with basil leafs.';

    vm.debug = function() {
      return Toast.debug(title, message);
    };
    vm.error = function() {
      return Toast.error(title, message);
    };
    vm.info = function() {
      return Toast.info(title, message);
    };
    vm.success = function() {
      return Toast.success(title, message);
    };
    vm.warning = function() {
      return Toast.warning(title, message);
    };

    activate();

    ////////////////

    function activate() {
      vm.pubmedEntries
        .then(function(response) {
          vm.pubmedEntries = response;
          return response;
        })
        .finally(function() {
          vm.loading = false;
        });
    }
  }

})();

