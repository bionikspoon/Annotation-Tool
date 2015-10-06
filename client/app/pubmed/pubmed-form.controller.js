class PubmedFormController {
  constructor($log, toastr, options) {
    'ngInject';

    this.$log = $log;
    this.toastr = toastr;
    this.options = options;


    this.loading = true;
    this.fields = options.actions.POST;

  }


}

export default PubmedFormController;
