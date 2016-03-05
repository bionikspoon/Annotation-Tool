(function() {
  'use strict';

  // PubmedEntries
  angular
    .module('app.pubmed')
    .directive('appPubmedEntries', pubmedPubmedEntriesDirective);

  /** @ngInject **/
  function pubmedPubmedEntriesDirective() {
    var directive = {
      bindToController: true,
      controller:       pubmedPubmedEntriesController,
      controllerAs:     'vm',
      templateUrl:      'app/pubmed/list/pubmedEntries.html',
      restrict:         'E',
      scope:            {
        entries: '=',
        canEdit: '&'
      }
    };
    return directive;

  }

  /** @ngInject **/
  function pubmedPubmedEntriesController() {}

})();

