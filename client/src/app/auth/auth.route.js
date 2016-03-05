(function() {
  'use strict';

  angular
    .module('app.auth')
    .config(authRoutes);

  /** @ngInject **/
  function authRoutes($stateProvider) {
    $stateProvider
      .state('auth', {
        url:      'auth/',
        abstract: true,
        parent:   'main',
        template: '<ui-view></ui-view>'
      })
      .state('auth.login', {
        url:          'login/',
        templateUrl:  'app/auth/login/authLogin.html',
        controller:   'authLoginController',
        controllerAs: 'vm',
        params:       {
          next: {
            value: null
          }
        },
        data:         {
          authenticate: false
        }
      })
      .state('auth.logout', {
        url:        'logout/',
        controller: 'authLogoutController',
        data:       {
          authenticate: true
        }
      })
      .state('auth.register', {
        url:          'register/',
        templateUrl:  'app/auth/register/authRegister.html',
        controller:   'authRegisterController',
        controllerAs: 'vm',
        data:         {
          authenticate: false
        }
      });
  }
})();
