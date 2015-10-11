export default function (toastr){
  // Set options third-party lib
  toastr.options.timeOut = 3000;
  toastr.options.positionClass = 'toast-bottom-right';
  toastr.options.preventDuplicates = true;
  toastr.options.progressBar = true;
}
