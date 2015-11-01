(function() {
  'use strict';

  angular
    .module('app.user')
    .service('UserStorage', UserStorage);

  /** @ngInject **/
  function UserStorage($timeout, SatellizerStorage) {
    this.get = get;
    this.set = set;
    this.remove = remove;


    var userKey = 'anno_user';

    ////////////////
    function get() {return JSON.parse(SatellizerStorage.get(userKey));}

    function set(user) {$timeout(SatellizerStorage.set(userKey, JSON.stringify(user)));}

    function remove() {SatellizerStorage.remove(userKey);}

  }

})();
