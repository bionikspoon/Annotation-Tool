export default function(RestangularProvider) {
  'ngInject';

  RestangularProvider.setBaseUrl('/api');
  RestangularProvider.setRestangularFields({
    selfLink: 'url'
  });
  RestangularProvider.addResponseInterceptor(pubmedOptionsInterceptor);
  RestangularProvider.setRequestSuffix('/');
}

function pubmedOptionsInterceptor(data, operation, what) {
  if(operation !== 'options' || what !== 'pubmed') {return data;}


  Object.keys(data.actions.POST)
        .forEach(key => data.actions.POST[key].name = key);
  return data;

}
