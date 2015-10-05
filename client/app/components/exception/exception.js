function exception(logger) {
  'ngInject';
  const service = {catcher};

  return service;

  function catcher(message) {
    return function(reason) {
      logger.error(message, reason);
    };
  }

}
export default exception;
