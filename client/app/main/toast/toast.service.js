'use strict';
class ToastService {
  constructor($mdToast, $q, $log) {
    'ngInject';
    this.$mdToast = $mdToast;
    this.$q = $q;
    this.$log = $log;
    this.baseToast = this.$mdToast.build()
                         .templateUrl('app/main/toast/toast.html')
                         .position('bottom right')
                         .controller(ToastController)
                         .controllerAs('toastCtrl')
                         .hideDelay(0);

    /*{
     templateUrl: 'app/main/toast/toast.html',
     position: 'bottom right',
     controller: ToastController,
     controllerAs: 'toastCtrl',
     bindToController: true,
     hideDelay: 0
     }*/
    ////this.debug = angular.bind(this, this.debug);
    //$log.debug('toast.service this:', this);
    $log.debug('toast.service this:', this);
  }

  _options(title, message, level, action = 'ok') {
    const data = () => ({
      title,
      message,
      level,
      action
    });
    return {
      templateUrl: 'app/main/toast/toast.html',
      position: 'bottom right',
      controller: ToastController,
      controllerAs: 'toastCtrl',
      bindToController: true,
      hideDelay: 0,
      resolve: {data}
    };
  }

  clear() {}

  debug(title, message) {
    this.$mdToast.show(this._options(title, message, 'debug'));
  }

  remove() {}

  error(title, message) {
    this.$mdToast.show(this._options(title, message, 'error'));
  }

  info(title, message) {
    this.$mdToast.show(this._options(title, message, 'info'));
  }

  success(title, message) {
    this.$mdToast.show(this._options(title, message, 'success'));
  }

  warning(title, message) {
    this.$mdToast.show(this._options(title, message, 'warning'));
  }

}

const meta = {
  debug: {
    icon: 'build',
    css: '',
    mod: 'app-toast--debug'
  },
  info: {
    icon: 'info',
    css: '',
    mod: 'app-toast--info'
  },
  success: {
    icon: 'done',
    css: '',
    mod: 'app-toast--success'
  },
  warning: {
    icon: 'warning',
    css: '',
    mod: 'app-toast--warning'
  },
  error: {
    icon: 'error',
    css: '',
    mod: 'app-toast--error'
  }
};
class ToastController {
  constructor($mdToast, $log, data) {
    'ngInject';
    this.$mdToast = $mdToast;
    //this.data = data.then(_data => this.data = _data);
    this.data = data;
    this.meta = meta[this.data.level || 'debug'];
  }

  hide() {
    this.$mdToast.hide();
  }
}
export default ToastService;
