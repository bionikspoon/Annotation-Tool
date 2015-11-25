(function() {
  'use strict';

  angular
    .module('app.layout')
    .config($mdThemingProviderConfig);

  /** @ngInject **/
  function $mdThemingProviderConfig($mdThemingProvider) {

    //noinspection JSUnresolvedFunction
    $mdThemingProvider
      .theme('default')
      .primaryPalette('indigo')
      .accentPalette('pink');

    //noinspection JSUnresolvedFunction
    $mdThemingProvider
      .theme('sidenav')
      .primaryPalette('blue-grey', {
        'hue-1': '400',
        'hue-2': '900'
      });

    //noinspection JSUnresolvedFunction
    $mdThemingProvider
      .theme('topnav')
      .primaryPalette('grey');
  }
})();
