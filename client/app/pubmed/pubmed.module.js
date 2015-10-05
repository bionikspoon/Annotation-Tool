import PubmedListController from './pubmed-list.controller';
import PubmedFormController from './pubmed-form.controller';
import PubmedItemController from './pubmed-item.controller';
import genericFormControlDirective from '../components/formControls/genericFormControl.directive';
import routerConfig from './pubmed.route';

angular.module('pubmed', [
    'ui.router', 'ngMaterial', 'restangular', 'main.exception'
  ])


  .controller('PubmedListController', PubmedListController)
  .controller('PubmedFormController', PubmedFormController)
  .controller('PubmedItemController', PubmedItemController)
  .directive('siteControlGeneric', () => new genericFormControlDirective())

  .config(routerConfig);
