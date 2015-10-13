(() => {
  describe('Pubmed Routes', () => {
    let $location;
    let $route;
    let $rootScope;
    beforeEach(module('pubmed.route'));
    beforeEach(inject((_$location_, _$route_, _$rootScope_) => {
      $location = _$location_;
      $route = _$route_;
      $rootScope = _$rootScope_;
    }));
    describe('list route', () => {
      let $httpBackend;
      beforeEach(inject((_$httpBackend_) => {
        $httpBackend = _$httpBackend_;
        $httpBackend.expectGET('views/home.html')
                    .respond(200, 'main.html');
      }));
    });
  });

})();
