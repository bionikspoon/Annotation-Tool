export default class MainController {
  constructor(Toast) {
    'ngInject';
    this.Toast = Toast;

    this.title = 'Ubi est azureus genetrix?';
    this.message = 'Who can shape the zen and futility of a visitor if he has the popular emptiness of the body?';
  }

  debug() {
    this.Toast.debug(this.title, this.message);
  }

  info() {
    this.Toast.info(this.title, this.message);
  }

  success() {
    this.Toast.success(this.title, this.message);
  }

  warning() {
    this.Toast.warning(this.title, this.message);
  }

  error() {
    this.Toast.error(this.title, this.message);
  }
}
