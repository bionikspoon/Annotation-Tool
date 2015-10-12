export default function AuthLogoutDirective($log, AuthService) {
  'ngInject';
  const directive = {
    restrict: 'A',
    link: link
  };
  return directive;
  //noinspection JSUnusedLocalSymbols
  function link(scope, element) {
    element.on('click', AuthService.logout);
  }
}
