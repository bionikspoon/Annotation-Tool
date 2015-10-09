function routerConfig($urlRouterProvider) {
  'ngInject';

  $urlRouterProvider.rule(appendTrailingSlash);
  $urlRouterProvider.otherwise('/');

}

function appendTrailingSlash($injector, $location) {
  'ngInject';
  const path = $location.url();
  if(path.endsWith('/') || path.indexOf('/?') > -1) {return;}

  if(path.indexOf('?') > -1) {return path.replace('?', '/?');}

  return path + '/';
}

export default routerConfig;
