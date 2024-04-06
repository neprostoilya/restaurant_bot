$(document).ready(function() {
    let selectedTable = false;

    $('.Table').click(function() {
        $(this).toggleClass('reserved');
        var tableValue = $(this).attr('value');
        $('.TextBottomP').text("Вы выбрали столик № " + tableValue);

        localStorage.setItem('selectedTable', tableValue);

        selectedTable = true; 
    });

    $('.ButtonWrapperAtable .ButtonWrapperTable').click(function(event) {
        if (!selectedTable) {
            $('.TextBottomP').text("Вы не выбрали столик!"); 
            return false; 
        }

        window.location.href = "{% url 'frontend:select_quantity_of_people_view' %}";
    });

    var storedTable = localStorage.getItem('selectedTable');
    if (storedTable) {
        $('.Table[value="' + storedTable + '"]').addClass('reserved');
        $('.TextBottomP').text("Вы выбрали столик № " + storedTable);

        selectedTable = true; 
    }
});
