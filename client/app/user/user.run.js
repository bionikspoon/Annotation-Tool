export default function(Session, $log, $rootScope, $q) {
  'ngInject';
  Session.create()
         .then(() =>  Session)
         .catch(error => $q.reject(error));
}
