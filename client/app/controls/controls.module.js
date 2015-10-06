
import genericInputDirective from './genericInput/genericInput.directive';
import radioGroupDirective from './radioGroup/radioGroup.directive';
import choiceSliderDirective from './choiceSlider/choiceSlider.directive';
import selectMultipleDirective from './selectMultiple/selectMultiple.directive';

angular.module('app.controls', ['ngMaterial'])
  .directive('appGenericInput', () => new genericInputDirective())
  .directive('appRadioGroup', () => new radioGroupDirective())
  .directive('appChoiceSlider', () => new choiceSliderDirective())
  .directive('appSelectMultiple', () => new selectMultipleDirective());
