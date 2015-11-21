(function() {
  'use strict';

  angular
    .module('app.pubmed')
    .factory('PubmedData', PubmedData);

  /** @ngInject **/
  function PubmedData($log, Restangular, $q) {
    var service = {
      options: options,
      list:    list,
      get:     get,
      init:    init,
      save:    save
    };
    return service;

    ////////////////

    function options() {
      var deferred = $q.defer();
      Restangular
        .all('pubmed')
        .options()
        .then(function(data) {
          return deferred.resolve(data.actions.POST);
        })
        .catch(function(error) {
          $log.error('PubmedData.factory error:', error);
          return deferred.reject(error);
        });

      return deferred.promise;
    }

    function list() {
      return $q.when(Restangular.all('pubmed').getList())
               .catch(handleError('list'));
    }

    function get(id) {
      return $q.when(Restangular.one('pubmed', id).get())
               .catch(handleError('get'));
    }

    function init() {
      return $q.when(Restangular.one('pubmed'))
               .catch(handleError('init'));
    }

    function save(model) {
      return $q.when(model.save())
               .catch(handleError('save'));
    }

    function handleError(message) {
      return function(error) {
        $log.debug('PubmedData::' + message + ' error:', error);
        return $q.reject(error);
      };
    }

  }

})();
