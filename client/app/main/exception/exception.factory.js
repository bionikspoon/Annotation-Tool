export default function exception($log, toastr) {
  'ngInject';
  const service = {catcher};
  return service;

  function catcher(message) {
    return function(reason) {
      $log.error(message, reason);
      $log.debug('exception.factory toastr:', toastr);
      toastr.error(reason.status + ' ' + reason.statusText || reason.toString(), message);
    };
  }
}
