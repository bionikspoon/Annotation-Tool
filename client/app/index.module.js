/* global require:false, toastr:false, moment:false */
import config from './index.config';

import routerConfig from './index.route';

import runBlock from './index.run';
import MainController from './main/main.controller';
import NavbarTop from './components/navbarTop/navbarTop.directive';
import NavbarSide from './components/navbarSide/navbarSide.directive';

require('./pubmed/pubmed.module');

angular.module('annotationTool', [
    'ngAnimate',
    'ngCookies',
    'ngTouch',
    'ngSanitize',
    'ui.router',
    'ngMaterial',
    'restangular',
    'pubmed'
  ])
  .constant('toastr', toastr)
  .constant('moment', moment)
  .config(config)

  .config(routerConfig)

  .run(runBlock)
  .directive('navbarTop', () => new NavbarTop())
  .directive('navbarSide', () => new NavbarSide())
  .controller('MainController', MainController);
