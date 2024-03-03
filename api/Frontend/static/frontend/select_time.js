$(document).ready(function() {
    function checkInput() {
      var timeInput = $('#floatingInputTime').val();
      
      if (timeInput) {
        $('.ButtonWrapper').removeAttr('disabled', 'disabled');
      } else {
        $('.ButtonWrapper').attr('disabled', 'disabled');
      }
    }
    $('#floatingInputTime').on('input', checkInput);
    checkInput();
  });
  