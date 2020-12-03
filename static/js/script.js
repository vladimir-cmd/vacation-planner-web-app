$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });

 $(document).ready(function(){
    $('.collapsible').collapsible();
    $(".tooltipped").tooltip();
    $('.datepicker').datepicker({
      format: "dd mmm, yyyy",
      yearRange: 10,
      showClearBtn: true,
      i18n: {
        done: "Select"
      }
    });
    $('select').formSelect();
  });