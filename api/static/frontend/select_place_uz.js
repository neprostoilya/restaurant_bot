$(document).ready(function() {
    let selectedPlace = false;

    $('.PlaceBtn').click(function(event) {
        event.preventDefault()
        $('.PlaceBtn').removeClass('selected'); 
        $(this).addClass('selected'); 
        var placeId = $(this).attr('value');
        var placeName = $(this).find('span').text();
        localStorage.setItem('selectedPlaceId', placeId);
        localStorage.setItem('selectedPlaceName', placeName);
        
        $('.TextBottomP').text("Siz " + placeName + " tanladingiz");

        selectedPlace = true;
        $('.ButtonWrapperAtable').removeClass('disabled'); 
    });

    $('.ButtonWrapperAtable .ButtonWrapperTable').click(function(event) {
        if (!selectedPlace) {
            return false;
        }

        window.location.href = "{% url 'frontend:select_quantity_of_people_view_uz' %}";
    });

    var selectedPlaceId = localStorage.getItem('selectedPlaceId');
    var selectedPlaceName = localStorage.getItem('selectedPlaceName');

    if (selectedPlaceId) {
        $('.PlaceBtn[value="' + selectedPlaceId + '"]').addClass('selected');
        $('.TextBottomP').text("Siz " + selectedPlaceName + " tanladingiz");
        selectedPlace = true;
        $('.ButtonWrapperAtable').removeClass('disabled');
    }
});