import exception from './exception/exception.factory';
import MainController from './main.controller';
import routerConfig from './main.route';

angular.module('app.main', ['ui.router', 'ngMaterial'])
  .config(routerConfig)
  .controller('MainController', MainController)
  .factory('exception', exception);
