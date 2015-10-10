import exception from './exception/exception.factory';
import MainController from './main.controller';
import routerConfig from './main.route';

import NavTopDirective from './navTop/mainNavTop.directive.js';
import NavSideDirective from './navSide/mainNavSide.directive.js';

angular.module('app.main', ['ui.router', 'ngMaterial'])
       .config(routerConfig)
       .controller('MainController', MainController)
       .factory('exception', exception)
       .directive('appNavTop', () => new NavTopDirective())
       .directive('appNavSide', () => new NavSideDirective());
