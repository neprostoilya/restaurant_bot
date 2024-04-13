$(document).ready(function() {
    let selectedTable = false;

    $('.Table').click(function() {
        $(this).toggleClass('reserved');
        var tableID = $(this).closest('.TableDiv').attr('value');
        var tableNumber = $(this).closest('.TableDiv').attr('data-number'); // Используем data-number для получения order.number
        console.log(tableID);
        $('.TextBottomP').text("Вы выбрали столик № " + tableNumber);

        localStorage.setItem('selectedTableText', tableNumber); // Сохраняем order.number
        localStorage.setItem('selectedTableNumber', tableID); // Сохраняем order.id

        selectedTable = true;
    });

    $('.ButtonWrapperAtable .ButtonWrapperTable').click(function(event) {
        if (!selectedTable) {
            $('.TextBottomP').text("Вы не выбрали столик!");
            return false;
        }

        window.location.href = "{% url 'frontend:select_quantity_of_people_view_ru' %}";
    });

    var selectedTableID = localStorage.getItem('selectedTableNumber');
    var selectedTableNumber = localStorage.getItem('selectedTableText');
    if (selectedTableID && selectedTableNumber) {
        $('.TableDiv[value="' + selectedTableID + '"] .Table').addClass('reserved');
        $('.TextBottomP').text("Вы выбрали столик № " + selectedTableNumber);

        selectedTable = true;
    }
});
