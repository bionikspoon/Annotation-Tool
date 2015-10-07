class PubmedFormController {
  constructor($log, options) {
    'ngInject';

    this.$log = $log;


    this.fields = {};
    angular.copy(options.actions.POST, this.fields);

    Object.keys(this.fields)
      .forEach(key => this.fields[key].name = key);
    this.entry = {};
    this.activate(options);

  }

  activate() {
  }


}

export default PubmedFormController;
