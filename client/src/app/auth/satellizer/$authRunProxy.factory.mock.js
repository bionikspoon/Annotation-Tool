(function() {
  'use strict';

  angular
    .module('app.auth')
    .config(function($provide) {
      $provide.factory('$authRunProxy', mock$authRunProxy);
    });

  /** @ngInject **/
  function mock$authRunProxy($q) {
    var service = {
      verify:          verify,
      isAuthenticated: isAuthenticated,
      can:             can
    };
    return service;

    ////////////////
    function verify() {
      this.resolve = null;
      this.reject = null;

      if(this.resolve !== null) {return $q.when(this.resolve);}
      if(this.reject !== null) {return $q.reject(this.reject);}

      return $q.reject({});
    }

    function isAuthenticated() {
      this.return = false;
      return this.return;
    }

    function can() {
      this.return = false;
      return this.return;
    }
  }

})();
