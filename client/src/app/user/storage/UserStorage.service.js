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
      var user = SatellizerStorage.get(userKey);
      return user ? JSON.parse(user) : user;
    }

    function set(user) {
      if(!angular.isObject(user)) {return;}
      SatellizerStorage.set(userKey, JSON.stringify(user));
    }

    function remove() {
      SatellizerStorage.remove(userKey);
    }

  }

})();
