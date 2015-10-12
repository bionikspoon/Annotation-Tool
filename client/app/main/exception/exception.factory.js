export default function exception($log, Toast) {
  'ngInject';
  const service = {catcher};
  return service;

  function catcher(message) {
    return function(reason) {
      $log.error(message, reason);
      Toast.error(reason.status + ' ' + reason.statusText || reason.toString(), message);
    };
  }
}
