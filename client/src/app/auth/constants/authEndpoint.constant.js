(function() {
  'use strict';
  var AUTH_ENDPOINT = {
    prefix:  '/api',
    login:   '/auth/login/',
    signup:  '/auth/signup/',
    profile: '/auth/profile/',
    refresh: '/auth/refresh/',
    verify:  '/auth/verify/'
  };
  join = join.bind(null, AUTH_ENDPOINT);
  AUTH_ENDPOINT.api = {
    login:   join('login'),
    signup:  join('signup'),
    profile: join('profile'),
    refresh: join('refresh'),
    verify:  join('verify')
  };

  function join(AUTH_ENDPOINT, key) {
    return AUTH_ENDPOINT.prefix + AUTH_ENDPOINT[key];
  }

  angular
    .module('app.auth')
    .constant('AUTH_ENDPOINT', AUTH_ENDPOINT);

})();
