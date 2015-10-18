export default function exceptionHandlerDecorator($provide) {
  'ngInject';
  $provide.decorator('$exceptionHandler', extendExceptionHandler);
}

function extendExceptionHandler($delegate, $injector) {
  'inject';
  return function(exception, cause) {
    const Toast = $injector.get('Toast');
    const errorData = {
      exception,
      cause
    };

    Toast.error(exception.msg, errorData);
    $delegate(exception, cause);
  };

}
