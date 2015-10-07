class PubmedFormController {
  constructor($log, options, Restangular) {
    'ngInject';

    this.$log = $log;
    this.Restangular = Restangular;
    this.fields = {};
    this.entry = {};

    Restangular.copy(options.actions.POST, this.fields);
  }


  submit(model) {
    //model.user = 'http://localhost:8000/api/users/196/';
    this.$log.debug('pubmed-item.controller model:', model);
    this.Restangular.all('pubmed')
      .post(model)
      .then(response => {
        this.$log.debug('pubmed-form.controller response:', response);
      })
      .catch(error => this.$log.error('pubmed-form.controller error:', error));
  }


}

export default PubmedFormController;
