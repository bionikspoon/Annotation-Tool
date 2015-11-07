(function() {
  'use strict';

  angular
    .module('app.layout')
    .factory('Toast', Toast);

  /** @ngInject **/
  function Toast($log, $mdToast, $q) {
    var toast = $q.when();
    var service = {
      debug:   debug,
      error:   error,
      info:    info,
      success: success,
      warning: warning,
      hide:    $mdToast.hide
    };
    return service;

    ////////////////

    function debug(title, message) {
      return show(buildToast(title, message, 'debug'));
    }

    function error(title, message) {
      return show(buildToast(title, message, 'error'));
    }

    function info(title, message) {
      return show(buildToast(title, message, 'info'));
    }

    function success(title, message) {
      return show(buildToast(title, message, 'success'));
    }

    function warning(title, message) {
      return show(buildToast(title, message, 'warning'));
    }

    ////////////////

    function buildToast(title, message, mod) {
      return $mdToast
        .build()
        .templateUrl('app/layout/toast/Toast.html')
        .hideDelay(3000)
        .position('bottom right')
        .controller(ToastController)
        .controllerAs('vm')
        .resolve({
          data: function() {
            return $q.when({
              title:   title,
              message: message,
              mod:     mod
            });
          }
        });
    }

    function show(build) {
      toast = $q.when(toast)
                .then(function() {
                  return $mdToast.show(build);
                });
      return toast;
    }
  }

  /** @ngInject **/
  function ToastController($log, Toast, data) {
    var definition = getDefinition(data.mod);
    var vm = this;
    vm.title = data.title;
    vm.message = data.message;
    vm.hide = Toast.hide;
    vm.icon = definition.icon;
    vm.mod = definition.mod;
    vm.action = 'X';

    activate();

    ////////////////

    function activate() {
      $log.debug('ToastController.activate vm:', vm);
    }

    ////////////////

    function getDefinition(mod) {
      var definition = {
        debug:   {
          icon: 'build',
          mod:  'app-toast--debug'
        },
        info:    {
          icon: 'info',
          mod:  'app-toast--info'
        },
        success: {
          icon: 'done',
          mod:  'app-toast--success'
        },
        warning: {
          icon: 'warning',
          mod:  'app-toast--warning'
        },
        error:   {
          icon: 'error',
          mod:  'app-toast--error'
        }
      };

      return definition[mod];
    }
  }

})();

