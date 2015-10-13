class PubmedFormController {
  constructor($log, $q, Restangular, Toast, $state, optionsPrepService) {
    'ngInject';

    this.$log = $log;
    this.$q = $q;
    this.Restangular = Restangular;
    this.Toast = Toast;
    this.fields = {};
    this.entry = {};
    this.errors = {};
    this.loading = true;
    this.$state = $state;

    const entryPromise = $state.params.id ? this.getEntry($state.params.id) : this.newEntry();
    const optionsPromise = this.setOptions(optionsPrepService);

    this.activate(entryPromise(), optionsPromise());

  }

  activate(entryPromise, optionsPromise) {
    this.$q.all([entryPromise, optionsPromise])
        .finally(() => this.loading = false);


  }


  submit(model) {
    model.userCtrl = 'http://localhost:8000/api/users/196/';

    model.save()
         .then(response => {
           this.Toast.success('Pubmed entry saved.');
           this.errors = {};
           this.$state.go('pubmed.list');
           return response;
         })
         .catch(error => {

           const msg = error.status + ' ' + error.statusText;
           this.Toast.error(msg, error.statusText);
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
    return () => this.Restangular.one('pubmed', id).get()
                     .then(entry => {
                       this.Restangular.copy(entry, this.entry);
                       return entry;
                     })
                     .catch(error => {
                       this.$log.error('pubmed-form.controller error:', error);
                       return error;
                     });
  }

  newEntry() {
    return () => this.$q.when(this.entry = this.Restangular.one('pubmed'));
  }

  setOptions(optionsPrepService) {
    return () => this.$q.when(angular.copy(optionsPrepService.actions.POST, this.fields));
  }
}

export default PubmedFormController;
