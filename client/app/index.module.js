/* global _:false, toastr:false, moment:false */
import exceptionHandlerDecorator  from './config/exceptionHandler.decorator';
import logProviderConfig          from './config/logProvider.config';
import mdThemingProviderConfig    from './config/mdThemingProvider.config';
import RestangularProviderConfig  from './config/RestangularProvider.config';
import toastrConfig               from './config/toastr.config';

import indexRoutes from './index.route';

import runBlock from './index.run';


angular.module('app', [
         'ngAnimate',
         'ngCookies',
         'ngTouch',
         'ngSanitize',
         'ui.router',
         'ngMaterial',
         'restangular',
         'app.main',
         'app.pubmed',
         'app.auth',
         'app.user'
       ])
       .constant('toastr', toastr)
       .constant('moment', moment)
       .constant('_', _)

       .config(exceptionHandlerDecorator)
       .config(logProviderConfig)
       .config(mdThemingProviderConfig)
       .config(RestangularProviderConfig)
       .config(toastrConfig)
       .config(indexRoutes)

       .run(runBlock);
