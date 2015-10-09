class PubmedFormController {
  constructor($log, Restangular, toastr, $state, optionsPrepService) {
    'ngInject';

    this.$log = $log;
    this.Restangular = Restangular;
    this.toastr = toastr;
    this.fields = {};
    this.entry = {};
    this.errors = {};
    this.loading = true;

    if($state.params.id) {this.getEntry($state.params.id);}
    angular.copy(optionsPrepService.actions.POST, this.fields);
  }


  submit(model) {
    model.user = 'http://localhost:8000/api/users/196/';
    this.$log.debug('pubmed-form.controller this:', this);
    this.Restangular.all('pubmed')
        .post(model)
        .then(response => {
          this.toastr.success('Pubmed entry saved.');
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

  getEntry(id) {
    this.Restangular.one('pubmed', id).get()
        .then(entry => {
          this.Restangular.copy(entry, this.entry);
          return entry;
        })
        .catch(error => {
          this.$log.error('pubmed-form.controller error:', error);
          return error;
        });
  }
}

export default PubmedFormController;
