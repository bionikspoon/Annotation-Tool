(function() {
  'use strict';

  angular
    .module('mock.AuthLoginData', [])
    .config(function($provide) {
      $provide.factory('AuthLoginData', mockAuthLoginData);
    });

  /** @ngInject **/
  function mockAuthLoginData($q) {
    var service = {
      options: options
    };
    return service;

    ////////////////

    function options() {
      return $q.when(getMockOptions());
    }

    function getMockOptions() {
      return Object.freeze({
        actions: {
          POST: {
            username: {
              type:       'string',
              required:   true,
              read_only:  false,
              label:      'Username',
              max_length: 128,
              name:       "username"
            },
            password: {
              type:      'password',
              required:  true,
              read_only: false,
              label:     'Password',
              name:      "password"
            }
          }
        }
      });
    }
  }

})();
