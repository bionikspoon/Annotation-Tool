import PubmedListController from './pubmed-list.controller';
import PubmedFormController from './pubmed-form.controller';
import PubmedItemController from './pubmed-item.controller';

import routerConfig from './pubmed.route';

angular.module('app.pubmed', [
    'ui.router', 'ngMaterial', 'restangular', 'app.controls'
  ])
  .config(routerConfig)

  .controller('PubmedListController', PubmedListController)
  .controller('PubmedFormController', PubmedFormController)
  .controller('PubmedItemController', PubmedItemController);
