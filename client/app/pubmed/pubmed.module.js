import PubmedListController from './pubmed-list.controller';
import PubmedFormController from './pubmed-form.controller';
import PubmedItemController from './pubmed-item.controller';
import genericInputDirective from '../components/formControls/genericInput.directive';
import radioGroupDirective from '../components/formControls/radioGroup.directive';
import choiceSliderDirective from '../components/formControls/choiceSlider.directive';
import selectMultipleDirective from '../components/formControls/selectMultiple.directive';

import routerConfig from './pubmed.route';

angular.module('app.pubmed', [
    'ui.router', 'ngMaterial', 'restangular'
  ])
  .config(routerConfig)

  .controller('PubmedListController', PubmedListController)
  .controller('PubmedFormController', PubmedFormController)
  .controller('PubmedItemController', PubmedItemController)
  .directive('appGenericInput', () => new genericInputDirective())
  .directive('appRadioGroup', () => new radioGroupDirective())
  .directive('appChoiceSlider', () => new choiceSliderDirective())
  .directive('appSelectMultiple', () => new selectMultipleDirective());
