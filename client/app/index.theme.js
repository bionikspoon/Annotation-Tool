function themeConfig($mdThemingProvider) {
  'ngInject';

  $mdThemingProvider.theme('default')
    .primaryPalette('indigo')
    .accentPalette('pink')
    .backgroundPalette('grey', {'default': '100'});

  $mdThemingProvider.theme('sidenav')
    .primaryPalette('blue-grey', {'hue-2': '900'});

  $mdThemingProvider.theme('topnav')
    .primaryPalette('grey');

}

export default themeConfig;
