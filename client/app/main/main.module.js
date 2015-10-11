/* global toastr:false */
import exception from './exception/exception.factory';
import MainController from './main.controller';
import mainRoutes from './main.route';

import NavTopDirective from './navTop/mainNavTop.directive.js';
import NavSideDirective from './navSide/mainNavSide.directive.js';

angular.module('app.main', ['ui.router', 'ngMaterial'])
       .config(mainRoutes)
       .constant('toastr', toastr)
       .controller('MainController', MainController)
       .factory('exception', exception)
       .directive('appNavTop', () => new NavTopDirective())
       .directive('appNavSide', () => new NavSideDirective());
