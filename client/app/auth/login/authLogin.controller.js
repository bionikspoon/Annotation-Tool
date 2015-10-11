class AuthLoginController {
  constructor($rootScope, $scope, $q, $log, $state, AUTH_EVENTS, AuthService) {
    'ngInject';

    this.$rootScope = $rootScope;
    this.userCtrl = $scope.userCtrl;
    this.$log = $log;
    this.$q = $q;
    this.$state = $state;
    this.AUTH_EVENTS = AUTH_EVENTS;
    this.AuthService = AuthService;
  }


  login(credentials) {
    this.AuthService.login(credentials)
        .then(user => {
          this.$state.go('pubmed.list');
        })
        .catch(error => {
          this.$q.reject(error);
        });
  }


}

export default AuthLoginController;
