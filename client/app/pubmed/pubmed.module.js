import PubmedListController from './list/pubmedList.controller';
import PubmedFormController from './form/pubmedForm.controller';
import PubmedItemController from './item/pubmedItem.controller';

import routerConfig from './pubmed.route';

angular.module('app.pubmed', ['ngAria', 'ui.router', 'ngMaterial', 'restangular', 'app.controls'])
       .config(routerConfig)
       .constant('toastr', toastr) // jshint ignore:line

       .controller('PubmedListController', PubmedListController)
       .controller('PubmedFormController', PubmedFormController)
       .controller('PubmedItemController', PubmedItemController);
