/* global KJUR */
(function() {
  'use strict';

  angular
    .module('mock.JWT', [])
    .factory('JWT', JWT);

  /** @ngInject **/
  function JWT() {
    var service = {
      generate: generate
    };
    return service;

    ////////////////

    function generate(user) {
      user = angular.isObject(user) ? user : {};

      var header = JSON.stringify({
        alg: 'HS256',
        typ: 'JWT'
      });
      var meta = {
        exp:      KJUR.jws.IntDate.get('now + 1hour'),
        orig_iat: KJUR.jws.IntDate.get('now'),
        user_id:  1,
        email:    "testUser@test.com",
        username: "testUser"
      };

      var payload = JSON.stringify(angular.merge(meta, user));
      var password = 'secret';

      return Object.freeze({token: KJUR.jws.JWS.sign('HS256', header, payload, password)});

    }
  }

})();
