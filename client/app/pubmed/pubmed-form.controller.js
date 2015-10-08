class PubmedFormController {
  constructor($log, options, Restangular, toastr) {
    'ngInject';

    this.$log = $log;
    this.Restangular = Restangular;
    this.toastr = toastr;
    this.fields = {};
    this.entry = {};
    this.errors = {};

    angular.copy(options.actions.POST, this.fields);
  }


  submit(model) {
    model.user = 'http://localhost:8000/api/users/196/';
    this.Restangular.all('pubmed')
      .post(model)
      .then(response => {
        this.errors = {};
        return response;
      })
      .catch(error => {

        const msg = error.status + ' ' + error.statusText;
        this.toastr.error(msg, error.statusText);
        if(error.status !== 400 || !Object.keys(error.data).length) {
          this.$log.error('Request failed, pubmed-form.controller error:', error);
          return error;
        }


        angular.copy(error.data, this.errors);
        this.$log.error('pubmed-form.controller this.errors:', this.errors);
        return error;

      });
  }


}

export default PubmedFormController;
