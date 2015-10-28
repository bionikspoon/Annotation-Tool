(function() {
  'use strict';

  angular
    .module('app.user')
    .factory('Session', Session);


  /** @ngInject **/
  function Session() {
    var service = {
      functionName: functionName
    };
    return service;

    ////////////////

    function functionName() {
    }
  }

})();

