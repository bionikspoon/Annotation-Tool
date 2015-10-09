import USER_ROLES from './userRoles.constant';
import UserController from './user.controller';
import Session from './session/session.service';

angular.module('app.user', [])
       .constant('USER_ROLES', USER_ROLES)
       .controller('UserController', UserController)
       .service('Session', Session);
