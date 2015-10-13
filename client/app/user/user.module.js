import USER_ROLES from './constants/userRoles.constant';
import SESSION_EVENTS from './constants/sessionEvents.constant';
import UserController from './user.controller';
import Session from './session/session.service';
import userRun from './user.run';

angular.module('app.user', [])
       .constant('USER_ROLES', USER_ROLES)
       .constant('SESSION_EVENTS', SESSION_EVENTS)
       .run(userRun)
       .controller('UserController', UserController)
       .service('Session', Session);
