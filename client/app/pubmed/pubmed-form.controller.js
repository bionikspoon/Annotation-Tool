class PubmedFormController {
  constructor($log, toastr, options) {
    'ngInject';

    this.$log = $log;
    this.toastr = toastr;
    this.options = options;


    this.loading = true;
    this.hello = 'hello';
    this.entry = {};
    this.activate();

  }

  activate() {
    //this.fields = this.options.actions.POST.map(option => {
    //  return option;
    //});

  }


}

export default PubmedFormController;
