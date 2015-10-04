/* global malarkey:false, toastr:false, moment:false */
import config from './index.config';

import routerConfig from './index.route';
import themeConfig from './index.theme';

import runBlock from './index.run';
import MainController from './main/main.controller';
import GithubContributorService from '../app/components/githubContributor/githubContributor.service';
import WebDevTecService from '../app/components/webDevTec/webDevTec.service';
import NavbarTop from '../app/components/navbarTop/navbarTop.directive';
import NavbarSide from '../app/components/navbarSide/navbarSide.directive';

angular.module('annotationTool',
  ['ngAnimate', 'ngCookies', 'ngTouch', 'ngSanitize', 'restangular', 'ui.router', 'ngMaterial'])
  .constant('malarkey', malarkey)
  .constant('toastr', toastr)
  .constant('moment', moment)
  .config(config)

  .config(routerConfig)
  .config(themeConfig)

  .run(runBlock)
  .service('githubContributor', GithubContributorService)
  .service('webDevTec', WebDevTecService)
  .controller('MainController', MainController)
  .directive('navbarTop', () => new NavbarTop())
  .directive('navbarSide', () => new NavbarSide());
