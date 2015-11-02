(function() {
  'use strict';

  angular
    .module('app.user')
    .service('UserStorage', UserStorage);

  /** @ngInject **/
  function UserStorage(SatellizerStorage) {
    var userKey = 'anno_user';

    this.get = get;
    this.set = set;
    this.remove = remove;

    ////////////////
    function get() {
      return JSON.parse(SatellizerStorage.get(userKey));
    }

    function set(user) {
      SatellizerStorage.set(userKey, JSON.stringify(user));
    }

    function remove() {
      SatellizerStorage.remove(userKey);
    }

  }

})();
