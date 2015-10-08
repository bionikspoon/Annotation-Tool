function config($logProvider, toastr, $mdThemingProvider, RestangularProvider, $provide) {
  'ngInject';
  // Enable log
  $logProvider.debugEnabled(true);


  $provide.decorator('$exceptionHandler', extendExceptionHandler);

  // Set options third-party lib
  toastr.options.timeOut = 3000;
  toastr.options.positionClass = 'toast-bottom-right';
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
  RestangularProvider.setRestangularFields({
    selfLink: 'url'
  });
  RestangularProvider.addResponseInterceptor(pubmedOptionsInterceptor);
  RestangularProvider.setRequestSuffix('/');
}
function pubmedOptionsInterceptor(data, operation, what) {
  if(operation !== 'options' && what !== 'pubmed') {return data;}

  Object.keys(data.actions.POST)
    .forEach(key => data.actions.POST[key].name = key);
  return data;

}

function extendExceptionHandler($delegate, toastr) {
  'ngInject';
  return function(exception, cause) {
    $delegate(exception, cause);
    const errorData = {
      exception,
      cause
    };

    toastr.error(exception.msg, errorData);
  };
}

export default config;
