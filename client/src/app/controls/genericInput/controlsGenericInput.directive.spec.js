(function() {
  'use strict';

  describe('controlsGenericInput.directive.spec', function() {
    beforeEach(module('app.controls'));
    var $compile;
    var $rootScope;
    var mockMeta = {
      "mock_integer":  {
        "type":      "integer",
        "required":  true,
        "read_only": false,
        "label":     "Mock Integer",
        "min_value": 0,
        "max_value": 2147483647,
        "name":      "mock_integer"
      },
      "mock_text":     {
        "type":       "string",
        "required":   false,
        "read_only":  false,
        "label":      "Mock Text",
        "max_length": 128,
        "name":       "mock_text"
      },
      "mock_textarea": {
        "type":      "string",
        "required":  false,
        "read_only": false,
        "label":     "Mock Textarea",
        "name":      "mock_textarea"
      }
    };

    beforeEach(inject(function(_$compile_, _$rootScope_) {
      $compile = _$compile_;
      $rootScope = _$rootScope_;
      $rootScope.meta = mockMeta;
    }));
    it('does stuff', function() {
      var element = $compile('<form app-form-meta=meta></form>');
    });

  });

})();
