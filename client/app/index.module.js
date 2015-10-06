/* global toastr:false, moment:false */
import config from './index.config';

import routerConfig from './index.route';

import runBlock from './index.run';
import NavbarTop from './components/navbarTop/navbarTop.directive';
import NavbarSide from './components/navbarSide/navbarSide.directive';


angular.module('app', [
    'ngAnimate', 'ngCookies', 'ngTouch', 'ngSanitize', 'ui.router', 'ngMaterial', 'restangular', 'app.main', 'app.pubmed'
  ])
  .constant('toastr', toastr)
  .constant('moment', moment)

  .config(config)
  .config(routerConfig)

  .run(runBlock)
  .directive('navbarTop', () => new NavbarTop())
  .directive('navbarSide', () => new NavbarSide());
