(function() {
  'use strict';

  angular
    .module('app.layout')
    .config($mdThemingProviderConfig);

  /** @ngInject **/
  function $mdThemingProviderConfig($mdThemingProvider) {

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
