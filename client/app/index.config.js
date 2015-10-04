function config($logProvider, toastr, $mdThemingProvider, RestangularProvider) {
  'ngInject';
  // Enable log
  $logProvider.debugEnabled(true);

  // Set options third-party lib
  toastr.options.timeOut = 3000;
  toastr.options.positionClass = 'toast-top-right';
  toastr.options.preventDuplicates = true;
  toastr.options.progressBar = true;


  // Angular Material theme config.
  $mdThemingProvider.theme('default')
    .primaryPalette('indigo')
    .accentPalette('pink');

  $mdThemingProvider.theme('sidenav')
    .primaryPalette('blue-grey', {'hue-2': '900'});

  $mdThemingProvider.theme('topnav')
    .primaryPalette('grey');

  RestangularProvider.setBaseUrl('/api');

}

export default config;
