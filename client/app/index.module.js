/* global toastr:false, moment:false */
import config from './index.config';

import routerConfig from './index.route';

import runBlock from './index.run';


angular.module('app', [
         'ngAnimate', 'ngCookies', 'ngTouch', 'ngSanitize', 'ui.router', 'ngMaterial', 'restangular', 'app.main', 'app.pubmed'
       ])
       .constant('toastr', toastr)
       .constant('moment', moment)
       .constant('_', _)


       .config(config)
       .config(routerConfig)

       .run(runBlock);
