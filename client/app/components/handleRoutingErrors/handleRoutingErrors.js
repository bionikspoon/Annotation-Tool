let handlingRoutingErrors = false;

function handleRoutingErrors($rootScope, $log, $location) {
  'ngInject';

  $rootScope.$on('$routeChangeError', (event, current, previous, rejection) => {
    if(handlingRoutingErrors) {return;}
    handlingRoutingErrors = true;
    const destination = (current && (current.title || current.name || current.loadedTemplateUrl)) || 'unknown target';
    const msg = 'Error routing to ' + destination + '. ' + (rejection.msg || '');

    $log.warning(msg, [current]);

    $location.path('/');
  });
}

export default handleRoutingErrors;
