$(document).ready(function() {
    function checkInput() {
      var timeInput = $('#floatingInputTime').val();
      
      if (timeInput.trim()) {
        $('.ButtonWrapper').removeAttr('disabled', 'disabled');
      } else {
        $('.ButtonWrapper').attr('disabled', 'disabled');
      }
    }
    $('#floatingInputTime').on('input', checkInput);
    checkInput();
  });
  