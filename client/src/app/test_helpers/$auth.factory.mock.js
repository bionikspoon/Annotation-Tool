(function() {
  'use strict';

  angular
    .module('mock.$auth', [])
    .config(function($provide) {
      $provide.factory('$auth', mock$auth);
    });

  /** @ngInject **/
  function mock$auth($q) {
    var service = {
      login:                 jasmine.createSpy('login').and.callFake(login),
      loginExpect:           getSet('loginCredentials'),
      loginResolve:          getSet('loginResolve'),
      loginReject:           getSet('loginReject'),
      isAuthenticated:       isAuthenticated,
      isAutheticatedResults: getSet('isAuthenticated')
    };
    var mock = mockInit();
    return service;

    ////////////////

    function login(credentials) {
      var deferred = $q.defer();
      var usernameMatch = credentials.username === mock.loginCredentials.username;
      var passwordMatch = credentials.password === mock.loginCredentials.password;
      if(usernameMatch && passwordMatch) {
        mock.isAuthenticated = true;
        deferred.resolve(mock.loginResolve);
      } else {
        mock.isAuthenticated = false;
        deferred.reject(mock.loginReject);
      }

      return deferred.promise;
    }

    function isAuthenticated() {
      return mock.isAuthenticated;
    }

    function getSet(key) {
      return function(value) {
        if(angular.isObject(value)) {
          mock[key] = angular.copy(value);
        } else if(angular.isDefined(value)) {
          mock[key] = value;
        }

        return mock[key];
      };
    }

    function mockInit() {
      return {
        loginCredentials: {
          username: 'admin',
          password: 'secret'
        },
        loginResolve:     {
          data:       {
            token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwidXNlcl9pZCI6MTk2LCJleHAiOjE0NDY1MTYyMDcsIm9yaWdfaWF0IjoxNDQ2NTE2MjAyLCJlbWFpbCI6ImFkbWluQGFubm8uY29tIn0.WUwfpgQnTUZ4gl2uLgduCRS14X_3V4oTQkZtYf5G4lE'
          },
          status:     200,
          statusText: 'OK'
        },
        loginReject:      {
          data:       {
            non_field_errors: ['Unable to login with provided credentials.']
          },
          status:     400,
          statusText: 'Bad Request'
        },
        isAuthenticated:  false
      };
    }
  }

})();
