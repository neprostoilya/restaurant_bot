$(document).ready(function() {
    let selectedTable = false;

    $('.Table').click(function() {
        $(this).toggleClass('reserved');
        var tableName = $(this).attr('data-name-table');
        localStorage.setItem('selectedTableName', tableName);

        $('.TextBottomP').text('Вы выбрали столик "' + tableName + '"');

        selectedTable = true;
    });

    $('.ButtonWrapperAtable .ButtonWrapperTable').click(function(event) {
        if (!selectedTable) {
            $('.TextBottomP').text("Вы не выбрали столик!");
            return false;
        }

        window.location.href = "{% url 'frontend:select_quantity_of_people_view_ru' %}";
    });

    var selectedTableName = localStorage.getItem('selectedTableName');
    if (selectedTableName) {
        $('.Table[data-name-table="' + selectedTableName + '" ]').addClass('reserved');
        $('.TextBottomP').text('Вы выбрали столик "' + selectedTableName + '"');

        selectedTable = true;
    }
});
