(function() {
  'use strict';

  describe('controlsFormMeta.directive.spec', function() {
    beforeEach(module('app.controls'));

    var $compile;
    var $rootScope;

    beforeEach(inject(function(_$compile_, _$rootScope_) {
      $compile = _$compile_;
      $rootScope = _$rootScope_;
    }));

    it('', function() {
      var element = $compile('<form app-form-meta=meta></form>')($rootScope);
      console.debug('controlsFormMeta.directive.spec element:', element);
      $rootScope.$digest();
      console.debug('controlsFormMeta.directive.spec element:', element);
    });

  });

})();
