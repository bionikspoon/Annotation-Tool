(function() {
  'use strict';

  angular
    .module('app.user')
    .service('UserStorage', UserStorage);

  /** @ngInject **/
  function UserStorage($log, SatellizerStorage) {
    var userKey = 'anno_user';

    this.get = get;
    this.set = set;
    this.remove = remove;

    ////////////////
    function get() {
      $log.debug('UserStorage.get this:', this);
      return JSON.parse(SatellizerStorage.get(userKey));
    }

    function set(user) {
      $log.debug('UserStorage.set this:', this);
      SatellizerStorage.set(userKey, JSON.stringify(user));
    }

    function remove() {
      SatellizerStorage.remove(userKey);
    }

  }

})();
