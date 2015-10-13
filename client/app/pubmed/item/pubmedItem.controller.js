class PubmedItemController {
  constructor(/*$log, Restangular*/) {
    'ngInject';
    //
    this.loading = true;
    this.entryOptions = {};
    //
    //Restangular.all('pubmed')
    //  .getList()
    //  .then(pubmedEntries => {
    //    this.pubmedEntries = pubmedEntries;
    //  })
    //  .catch(error => {
    //    $log.error('error:', error);
    //  })
    //  .finally(()=>this.loading = false);
    this.activate();
  }

  activate(){}

}

export default PubmedItemController;
