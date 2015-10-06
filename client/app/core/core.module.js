import exception from './exception/exception.factory';
import CoreController from './core.controller';
import routerConfig from './core.route';

angular.module('app.core', ['ui.router', 'ngMaterial'])
  .config(routerConfig)
  .controller('CoreController', CoreController)
  .factory('exception', exception);
