class PubmedListController {
  constructor($log, Restangular) {
    'ngInject';

    this.loading = true;
    this.pubmedEntries = [];

    Restangular.all('pubmed')
      .getList()
      .then(pubmedEntries => {
        this.pubmedEntries = pubmedEntries;
      })
      .catch(error => {
        $log.error('error:', error);
      })
      .finally(()=>this.loading = false);

  }

}

export default PubmedListController;
