class MainController {
  constructor($timeout, webDevTec, toastr, $mdSidenav) {
    'ngInject';

    this.awesomeThings = [];
    this.classAnimation = '';
    this.creationDate = 1443810483786;
    this.toastr = toastr;
    this.$mdSidenav = $mdSidenav;


    this.activate($timeout, webDevTec);
  }

  activate($timeout, webDevTec) {
    this.getWebDevTec(webDevTec);
    $timeout(() => {
      this.classAnimation = 'rubberBand';
    }, 4000);
  }

  getWebDevTec(webDevTec) {
    this.awesomeThings = webDevTec.getTec();

    angular.forEach(this.awesomeThings, (awesomeThing) => {
      awesomeThing.rank = Math.random();
    });
  }

  showToastr() {
    this.toastr.info(
      'Fork <a href="https://github.com/Swiip/generator-gulp-angular" target="_blank"><b>generator-gulp-angular</b></a>');
    this.classAnimation = '';
  }

  toggleSidenav() {
    this.$mdSidenav('left')
      .toggle();
  }
  openMenu($mdOpenMenu, e) {
    $mdOpenMenu(e);
  }
}

export default MainController;
