/*@ngInject*/
function exception($log, toastr) {
  const service = {catcher};

  return service;

  function catcher(message) {
    return function(reason) {
      $log.error(message, reason);
      toastr.error(reason.status + ' ' + reason.statusText || reason.toString(), message);
    };
  }

}
export default exception;
