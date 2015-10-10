export default function AuthLogoutDirective($log, AuthService) {
  'ngInject';
  const directive = {
    restrict: 'A',
    link: link
  };
  return directive;
  function link(_, element) {
    element.on('click', AuthService.logout);
  }
}
