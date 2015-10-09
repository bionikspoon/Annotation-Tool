import routerConfig from './auth.route';
import AUTH_EVENTS from './constants/authEvents.constant.js';
import AUTH_ROLES from './constants/authRoles.constant.js';
import AuthLoginController from './login/authLogin.controller.js';
import AuthService from './auth.service';
import AuthSession from './session/authSession.service';
angular.module('app.auth', [])
       .config(routerConfig)
       .constant('AUTH_EVENTS', AUTH_EVENTS)
       .constant('AUTH_ROLES', AUTH_ROLES)
       .controller('AuthLoginController', AuthLoginController)
       .service('AuthService', AuthService)
       .service('AuthSession', AuthSession);
