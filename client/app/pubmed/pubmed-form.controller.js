const diseaseData = [
  {
    "value": "http://localhost:8000/api/lookup-disease/1/",
    "display_name": "Adenocarcinoma Of Lung"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/2/",
    "display_name": "Carcinoma Of Ampulla Of Vater"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/3/",
    "display_name": "Carcinoma Of Colon"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/4/",
    "display_name": "Extragastrointestinal Stromal Tumor Of Peritoneum"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/5/",
    "display_name": "Glioma"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/6/",
    "display_name": "Hashimoto Thyroiditis"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/7/",
    "display_name": "Malignant Glioma Of Brain"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/8/",
    "display_name": "Malignant Melanoma"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/9/",
    "display_name": "Malignant Melanoma Of Conjunctiva"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/10/",
    "display_name": "Malignant Tumor Of Thyroid Gland"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/11/",
    "display_name": "Metastasis From Malignant Tumor Of Colon"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/12/",
    "display_name": "Metastasis From Malignant Tumor Of Rectum"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/13/",
    "display_name": "Metastatic Malignant Melanoma"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/14/",
    "display_name": "Neoplasm Of Colon"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/15/",
    "display_name": "Neoplasm Of Ovary"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/16/",
    "display_name": "Neoplastic Disease"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/17/",
    "display_name": "Non-Small Cell Lung Cancer"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/18/",
    "display_name": "Papillary Thyroid Carcinoma"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/19/",
    "display_name": "Primary Adenocarcinoma Of Pancreas"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/20/",
    "display_name": "Secondary Malignant Neoplasm Of Brain"
  }, {
    "value": "http://localhost:8000/api/lookup-disease/21/",
    "display_name": "Serous Cystadenoma Of Ovary"
  }
];

class PubmedFormController {
  constructor($log) {
    'ngInject';

    this.$log = $log;
    this.diseaseChoices = [];
    this.disease = [];
    this.activate();
  }


  activate() {
    this.diseaseChoices = diseaseData.map(disease => {
      disease._lowername = disease.display_name.toLowerCase();
      return disease;
    });
  }

  querySearch(query) {

    return query ? this.diseaseChoices.filter(this.createFilterFor(query)) : this.diseaseChoices;
  }

  createFilterFor(query) {
    let lowerCaseQuery = angular.lowercase(query);
    return function filterFn(disease) {
      return (disease._lowername.indexOf(lowerCaseQuery) === 0);
    };

  }

  selectedItemChange(item) {
    this.$log.info('Select item changed to ' + JSON.stringify(item));
  }

}

export default PubmedFormController;
