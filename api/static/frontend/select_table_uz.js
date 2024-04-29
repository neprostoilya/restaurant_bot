$(document).ready(function() {
    let selectedTable = false;

    $('.Table').click(function() {
        $(this).toggleClass('reserved');
        var tableName = $(this).attr('data-name-table');
        localStorage.setItem('selectedTableName', tableName);
        
        $('.TextBottomP').text("Siz " + tableName + " stolni tanladingiz");

        selectedTable = true;
    });

    $('.ButtonWrapperAtable .ButtonWrapperTable').click(function(event) {
        if (!selectedTable) {
            $('.TextBottomP').text("Siz stolni tanlamadingiz!");
            return false;
        }

        window.location.href = "{% url 'frontend:select_quantity_of_people_view_uz' %}";
    });

    var selectedTableName = localStorage.getItem('selectedTableName');
    if (selectedTableName) {
        $('.Table[data-name-table="' + selectedTableName + '" ]').addClass('reserved');
        $('.TextBottomP').text("Siz " + selectedTableName + " stolni tanladingiz");

        selectedTable = true;
    }
});
