$(document).ready(function() {
  let selectedTable = false;

  $('.Table').click(function() {
    $(this).toggleClass('reserved');
    var tableValue = $(this).attr('value');
    $('.TextBottomP').text("Вы выбрали столик № " + tableValue);
    
    selectedTable = !selectedTable; 
  });

  $('.ButtonWrapper').click(function(event) {
    if (!selectedTable) {
      $('.TextBottomP').text("Вы не выбрали столик!");
    }
  });
});
