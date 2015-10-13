import mainRoutes from './main.route';

import MainController from './main.controller';

import TopnavDirective from './topnav/mainTopnav.directive.js';
import SidenavDirective from './sidenav/mainSidenav.directive.js';

import ToastService from './toast/toast.service';
import exception from './exception/exception.factory';

angular.module('app.main', ['ui.router', 'ngMaterial'])
       .config(mainRoutes)
       .controller('MainController', MainController)
       .directive('appTopnav', () => new TopnavDirective())
       .directive('appSidenav', () => new SidenavDirective())
       .factory('exception', exception)
       .service('Toast', ToastService);
