export default function(Session, $log, $rootScope, $q) {
  'ngInject';
  Session.create()
         .then(success=> {
           $log.debug('user.run success:', success);
           $log.debug('user.run Session:', Session);
           return Session;
         })
         .catch(error => {
           $log.error('user.run error:', error);
           $log.debug('user.run Session:', Session);

           return $q.reject(error);

         });
}
