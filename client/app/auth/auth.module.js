import routerConfig from './auth.route';
import AUTH_EVENTS from './constants/authEvents.constant.js';
import AuthLoginController from './login/authLogin.controller.js';
import AuthService from './auth.service';
angular.module('app.auth', ['app.user'])
       .config(routerConfig)
       .constant('AUTH_EVENTS', AUTH_EVENTS)
       .controller('AuthLoginController', AuthLoginController)
       .service('AuthService', AuthService);
