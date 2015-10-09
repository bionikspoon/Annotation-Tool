import exception from './exception/exception.factory';
import MainController from './main.controller';
import routerConfig from './main.route';

import NavbarTop from '../components/navbar/navbarTop.directive';
import NavbarSide from '../components/navbar/navbarSide.directive';

angular.module('app.main', ['ui.router', 'ngMaterial'])
       .config(routerConfig)
       .controller('MainController', MainController)
       .factory('exception', exception)
       .directive('appNavbarTop', () => new NavbarTop())
       .directive('appNavbarSide', () => new NavbarSide());
