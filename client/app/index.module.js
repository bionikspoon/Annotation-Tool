/* global toastr:false, moment:false */
import config from './index.config';

import routerConfig from './index.route';

import runBlock from './index.run';
import MainController from './main/main.controller';
import PubmedListController from './pubmed/pubmed.list.controller';
import PubmedFormController from './pubmed/pubmed.form.controller';
import PubmedItemController from './pubmed/pubmed.item.controller';
import NavbarTop from './components/navbarTop/navbarTop.directive';
import NavbarSide from './components/navbarSide/navbarSide.directive';

angular.module('annotationTool',
  ['ngAnimate', 'ngCookies', 'ngTouch', 'ngSanitize', 'ui.router', 'ngMaterial', 'restangular'])
  .constant('toastr', toastr)
  .constant('moment', moment)
  .config(config)

  .config(routerConfig)

  .run(runBlock)
  .directive('navbarTop', () => new NavbarTop())
  .directive('navbarSide', () => new NavbarSide())
  .controller('MainController', MainController)
  .controller('PubmedListController', PubmedListController)
  .controller('PubmedFormController', PubmedFormController)
  .controller('PubmedItemController', PubmedItemController);
