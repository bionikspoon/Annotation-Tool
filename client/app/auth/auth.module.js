import routerConfig from './auth.route';
import AuthLoginController from './login/authLogin.controller.js';
angular.module('app.auth', [])
       .config(routerConfig)
       .controller('AuthLoginController', AuthLoginController);
