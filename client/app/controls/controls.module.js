import GenericInputDirective from './genericInput/genericInput.directive';
import RadioGroupDirective from './radioGroup/radioGroup.directive';
import ChoiceSliderDirective from './choiceSlider/choiceSlider.directive';
import SelectMultipleDirective from './selectMultiple/selectMultiple.directive';
import FormMetaDirective from './formMeta/formMeta.directive';

angular.module('app.controls', ['ngMaterial'])
  .directive('appGenericInput', () => new GenericInputDirective())
  .directive('appRadioGroup', () => new RadioGroupDirective())
  .directive('appChoiceSlider', () => new ChoiceSliderDirective())
  .directive('appSelectMultiple', () => new SelectMultipleDirective())
  .directive('appFormMeta', () => new FormMetaDirective())
