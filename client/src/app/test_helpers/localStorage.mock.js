/* global localStorage */
(function() {
  'use strict';

  angular
    .module('mock.localStorage', [])
    .run(mockLocalStorage);

  function mockLocalStorage() {
    var storage = {};

    spyOn(localStorage, 'getItem').and.callFake(function(key) {
      return storage[key] || '';
    });
    spyOn(localStorage, 'setItem').and.callFake(function(key, value) {
      storage[key] = value + '';
    });
    spyOn(localStorage, 'removeItem').and.callFake(function(key) {
      delete storage[key];

    });
    spyOn(localStorage, 'clear').and.callFake(function() {
      storage = {};
    });
  }
})();
