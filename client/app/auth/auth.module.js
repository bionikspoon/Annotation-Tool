import authRoutes from './auth.route';
import authConfig from './auth.config';
import authRun from './auth.run';
import AUTH_EVENTS from './events/authEvents.constant.js';
import AuthLoginController from './login/authLogin.controller.js';
import AuthService from './auth.service';
import AuthInterceptorService from './interceptor/AuthInterceptor.service';
angular.module('app.auth', ['app.user'])
       .constant('AUTH_EVENTS', AUTH_EVENTS)
       .config(authRoutes)
       .config(authConfig)
       .run(authRun)
       .controller('AuthLoginController', AuthLoginController)
       .service('AuthService', AuthService)
       .service('AuthInterceptorService', AuthInterceptorService);
