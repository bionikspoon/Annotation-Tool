(function() {
  'use strict';

  angular
    .module('mock.UserStorage', ['mock.localStorage'])
    .config(userDecorator);

  /** @ngInject **/
  function userDecorator($provide) {
    $provide.decorator('UserStorage', decorateUserStorage);
  }

  /** @ngInject **/
  function decorateUserStorage($delegate) {
    spyOn($delegate, 'get').and.callThrough();
    spyOn($delegate, 'set').and.callThrough();
    spyOn($delegate, 'remove').and.callThrough();
    return $delegate;
  }

})();
