import genericInputDirective from './genericInput/genericInput.directive';
import radioGroupDirective from './radioGroup/radioGroup.directive';
import choiceSliderDirective from './choiceSlider/choiceSlider.directive';
import selectMultipleDirective from './selectMultiple/selectMultiple.directive';
import formMetaDirective from './formMeta/formMeta.directive';

angular.module('app.controls', ['ngMaterial', 'ngMessages', 'ngAria'])
       .constant('_', _)
       .directive('appGenericInput', genericInputDirective)
       .directive('appRadioGroup', radioGroupDirective)
       .directive('appChoiceSlider', choiceSliderDirective)
       .directive('appSelectMultiple', selectMultipleDirective)
       .directive('appFormMeta', formMetaDirective);
