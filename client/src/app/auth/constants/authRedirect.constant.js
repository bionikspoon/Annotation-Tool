(function() {
  'use strict';

  angular
    .module('app.auth')
    .constant('AUTH_REDIRECT', {
      postLogin:  'pubmed.list',
      postLogout: 'pubmed.list'
    });
})();
