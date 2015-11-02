(function() {
  'use strict';

  angular
    .module('mock.UserData', [])
    .config(function($provide) {
      $provide.service('UserData', mockUserData);
    });

  /** @ngInject **/
  function mockUserData($q) {
    this.mockUser = {};
    this.reject = false;
    this.get = get;
    spyOn(this, 'get').and.callThrough();

    ////////////////

    function get() {
      if(this.reject) {
        return $q.reject('hello');
      }
      return $q.when(this.mockUser);
    }
  }

})();
