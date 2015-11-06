(function() {
  'use strict';

  angular
    .module('app.auth')
    .constant('AUTH_ENDPOINTS', {
      prefix:  '/api',
      login:   '/auth/login/',
      signup:  '/auth/signup/',
      profile: '/auth/profile/',
      refresh: '/auth/refresh/',
      verify:  '/auth/verify/'

    });
})();
