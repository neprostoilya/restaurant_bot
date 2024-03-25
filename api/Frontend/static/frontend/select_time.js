$(document).ready(function() {
    function checkInput() {
        var timeInput = $('#floatingInputTime').val();
        
        if (timeInput && validateTimeFormat(timeInput)) {
            $('.ButtonWrapper').removeAttr('disabled');
            localStorage.setItem('selectedTime', timeInput);
        } else {
            $('.ButtonWrapper').attr('disabl    ed', 'disabled');
        }
    }

    $('#floatingInputTime').on('input', checkInput);

    var storedTime = localStorage.getItem('selectedTime');
    if (storedTime && validateTimeFormat(storedTime)) {
        $('#floatingInputTime').val(storedTime);
    }

    checkInput();
});

function validateTimeFormat(time) {
    var pattern = /^([01]?[0-9]|2[0-3]):[0-5][0-9]$/;
    return pattern.test(time);
}