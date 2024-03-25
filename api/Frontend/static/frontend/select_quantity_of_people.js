$(document).ready(function() {
    $('#typeNumber').on('input', function() {
        var peopleCount = $(this).val();
        
        localStorage.setItem('selectedPeopleCount', peopleCount);
    });
    
    var storedPeopleCount = localStorage.getItem('selectedPeopleCount');
    if (storedPeopleCount) {
        $('#typeNumber').val(storedPeopleCount);
    }

    $('.ButtonWrapperQuantityPeople').click(function(event) {
        if ($('#typeNumber').val() === '') {
            alert('Вы не ввели количество людей!');
        } else {
            let tg = window.Telegram.WebApp; 
            tg.sendData('TEST');
            tg.close();
        }
    });
});

