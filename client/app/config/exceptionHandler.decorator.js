export default function exceptionHandlerDecorator($provide) {
  'ngInject';
  $provide.decorator('$exceptionHandler', extendExceptionHandler);
}

function extendExceptionHandler($delegate, toastr) {
  'inject';
  return function(exception, cause) {
    const errorData = {
      exception,
      cause
    };
    toastr.error(exception.msg, errorData);
    $delegate(exception, cause);
  };

}
