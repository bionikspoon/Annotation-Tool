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
    return {
      debug: this.debug.bind(this),
      error: this.error.bind(this),
      info: this.info.bind(this),
      success: this.success.bind(this),
      warning: this.warning.bind(this)
    };
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
      hideDelay: 3000,
      resolve: {data}
    };
  }


  debug(title, message) {
    return this.$mdToast.show(this._options(title, message, 'debug'));
  }


  error(title, message) {
    return this.$mdToast.show(this._options(title, message, 'error'));
  }

  info(title, message) {
    return this.$mdToast.show(this._options(title, message, 'info'));
  }

  success(title, message) {
    return this.$mdToast.show(this._options(title, message, 'success'));
  }

  warning(title, message) {
    return this.$mdToast.show(this._options(title, message, 'warning'));
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
  constructor($mdToast, data) {
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
