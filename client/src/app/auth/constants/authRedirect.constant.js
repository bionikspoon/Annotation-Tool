(function() {
  'use strict';

  angular
    .module('app.auth')
    .constant('REDIRECT', {
      postLogin:  'pubmed.list',
      postLogout: 'pubmed.list'
    });
})();
