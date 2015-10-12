/* global toastr:false */
import mainRoutes from './main.route';

import MainController from './main.controller';

import NavTopDirective from './navTop/mainNavTop.directive.js';
import NavSideDirective from './navSide/mainNavSide.directive.js';

import ToastService from './toast/toast.service';
import exception from './exception/exception.factory';

angular.module('app.main', ['ui.router', 'ngMaterial'])
       .config(mainRoutes)
       .constant('toastr', toastr)
       .controller('MainController', MainController)
       .directive('appNavTop', () => new NavTopDirective())
       .directive('appSidenav', () => new NavSideDirective())
       .factory('exception', exception)
       .service('Toast', ToastService);
