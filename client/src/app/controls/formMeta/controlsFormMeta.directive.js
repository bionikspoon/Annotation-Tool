(function() {
  'use strict';

  // formMeta
  angular
    .module('app.controls')
    .directive('appFormMeta', controlsFormMetaDirective);

  /** @ngInject **/
  function controlsFormMetaDirective() {
    var directive = {
      bindToController: true,
      controller:       controlsFormMetaController,
      controllerAs:     'vm',
      restrict:         'A',
      scope:            {
        meta: '&appFormMeta',
        form: '=name'
      }
    };
    return directive;
  }

  /** @ngInject **/
  function controlsFormMetaController($q, $log, $scope, $timeout) {
    var vm = this;

    activate();

    ////////////////

    function activate() {
      var deferred = $q.defer();

      $timeout(function() {
        if($scope.form && $scope.meta) {
          deferred.resolve({
            form: $scope.form,
            meta: $scope.meta()
          });
        } else {
          if(!$scope.form) {
            $log.error('formMeta.directive $scope.form:', $scope.form);
          }
          if(!$scope.meta) {
            $log.error('formMeta.directive $scope.meta:', $scope.meta);
          }
          deferred.reject('`form` or `meta` are not in current scope.');
        }
      });

      return deferred.promise;

    }

  }

})();

