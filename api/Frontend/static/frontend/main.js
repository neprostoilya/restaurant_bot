$(document).ready(function() {
    $('.add-to-cart-button').click(function(e) {
      e.preventDefault();
      var csrfmiddlewaretoken = $(this).siblings('input[name="csrfmiddlewaretoken"]').val();
      var user = String($(this).siblings('input[name="user"]').val());
      var dish = String($(this).siblings('input[name="dish"]').val());
      var quantity = String($(this).siblings('input[name="quantity"]').val());
      $.ajax({
        type: 'POST',
        url: '/carts/create_cart/',
        data: {
          dish: String(dish),
          user: String(user),
          quantity: String(quantity), 
          csrfmiddlewaretoken: csrfmiddlewaretoken
        },
      });
    });
  });
  