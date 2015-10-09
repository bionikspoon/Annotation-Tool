import routerConfig from './auth.route';
import AuthLoginController from './login/AuthLogin.controller';
angular.module('app.auth', [])
       .config(routerConfig)
       .controller('AuthLoginController', AuthLoginController);
