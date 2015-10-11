function indexRoutes($urlRouterProvider) {
  'ngInject';

  $urlRouterProvider.rule(appendTrailingSlash);
  $urlRouterProvider.otherwise('/');


}
function appendTrailingSlash($injector) {
  'ngInject';
  const $location = $injector.get('$location');
  const path = $location.url();
  if(path.endsWith('/') || path.indexOf('/?') > -1) {return;}

  if(path.indexOf('?') > -1) {return path.replace('?', '/?');}

  return path + '/';
}
export default indexRoutes
