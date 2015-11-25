(function() {
  'use strict';

  angular
    .module('app.layout')
    .factory('Toast', Toast);

  /** @ngInject **/
  function Toast($mdToast, $q) {
    var toast = $q.when();
    var service = {
      debug:   debug,
      error:   error,
      info:    info,
      success: success,
      warning: warning,
      hide:    $mdToast.hide,
      resolve: {
        debug:   resolve('debug'),
        error:   resolve('error'),
        info:    resolve('info'),
        success: resolve('success'),
        warning: resolve('warning')
      },
      reject:  {
        debug:   reject('debug'),
        error:   reject('error'),
        info:    reject('info'),
        success: reject('success'),
        warning: reject('warning')

      }
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

    function resolve(mod) {
      return function resolveDecorator(title, message) {
        return function(response) {
          service[mod](title, message);
          return $q.when(response);
        };
      };
    }

    function reject(mod) {
      return function rejectDecorator(title, message) {
        return function(error) {
          service[mod](title, message);
          return $q.reject(error);
        };
      };
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
  function ToastController(Toast, data) {
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

    function activate() {}

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

