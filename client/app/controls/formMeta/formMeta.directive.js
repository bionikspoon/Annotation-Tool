function formMetaDirective() {
  'ngInject';

  let directive = {
    restrict: 'A',
    controller: FormMetaController,
    controllerAs: 'vm',
    scope: {
      meta: '&appFormMeta',
      form: '=name'
    }
  };
  return directive;
}


class FormMetaController {
  constructor($q, $log, $scope, $timeout) {
    'ngInject';
    const deferred = $q.defer();

    $timeout(() => {
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

export default formMetaDirective;
