import authRoutes from './auth.route';
import authRun from './auth.run';
import AUTH_EVENTS from './events/authEvents.constant.js';
import AuthLoginController from './login/authLogin.controller.js';
import AuthService from './auth.service';
import AuthLogoutDirective from './logout/authLogout.directive';
import httpProviderConfig from './config/httpProvider.config';

angular.module('app.auth', ['app.user', 'ui.router'])
       .constant('AUTH_EVENTS', AUTH_EVENTS)
       .config(authRoutes)
       .config(httpProviderConfig)
       .run(authRun)
       .controller('AuthLoginController', AuthLoginController)
       .service('AuthService', AuthService)
       .directive('appAuthLogout', AuthLogoutDirective);
