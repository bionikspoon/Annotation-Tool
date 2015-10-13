/* global console:false */
const ACTIVE = false;
export default function rootScopeDecorator($provide) {
  'ngInject';
  if(ACTIVE) {
    $provide.decorator('$rootScope', extendRootScope);
  }
}
function extendRootScope($delegate) {

  const Scope = $delegate.constructor;
  const _broadcast = Scope.prototype.$broadcast;
  const _emit = Scope.prototype.$emit;

  Scope.prototype.$broadcast = function() {
    if(angular.isDefined(arguments[0])) {
      console.debug('$broadcast:', arguments);
    } else {
      console.warn('$broadcast:', arguments, this);
    }
    return _broadcast.apply(this, arguments);
  };

  Scope.prototype.$emit = function() {
    console.debug('$emit:', arguments);
    return _emit.apply(this, arguments);
  };

  return $delegate;
}
