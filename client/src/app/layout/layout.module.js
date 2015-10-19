(function() {
  'use strict';
  angular.module('app.layout', ['ngMaterial'])
         .config(layoutConfig);

  /* @ngInject */
  function layoutConfig($mdThemingProvider) {
    $mdThemingProvider
      .theme('default')
      .primaryPalette('indigo')
      .accentPalette('pink');

    $mdThemingProvider
      .theme('sidenav')
      .primaryPalette('blue-grey', {
        'hue-1': '400',
        'hue-2': '900'
      });

    $mdThemingProvider
      .theme('topnav')
      .primaryPalette('grey');
  }
})();
(function() {
  'use strict';
  // Topnav
  angular
    .module('app.layout')
    .directive('appTopnav', topnavDirective);

  /* @ngInject */
  function topnavDirective() {
    var directive = {
      bindToController: true,
      controller:       topnavController,
      controllerAs:     'vm',
      link:             link,
      restrict:         'A',
      scope:            {}
    };
    return directive;

    function link(scope, element, attrs) {

    }
  }

  /* @ngInject */
  function topnavController() {

  }

})();



