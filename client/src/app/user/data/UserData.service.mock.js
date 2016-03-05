(function() {
  'use strict';

  angular
    .module('mock.UserData', [])
    .config(function($provide) {
      $provide.service('UserData', mockUserData);
    });

  /** @ngInject **/
  function mockUserData($q) {
    var self = this;
    self.mockUser = {};
    self.reject = false;
    self.get = get;
    spyOn(this, 'get').and.callThrough();

    ////////////////

    function get() {
      if(self.reject) {
        return $q.reject('hello');
      }
      return $q.when(self.mockUser);
    }
  }

})();
