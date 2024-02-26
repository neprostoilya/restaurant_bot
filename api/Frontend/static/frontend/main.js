$(document).ready(function() {
    $('.add-to-cart-button').click(function(e) {
      e.preventDefault();
      var csrfmiddlewaretoken = $(this).siblings('input[name="csrfmiddlewaretoken"]').val();
      var user = String($(this).siblings('input[name="user"]').val());
      var dish = String($(this).siblings('input[name="dish"]').val());
      var num = String($(this).siblings('input[name="num"]').val());
      $.ajax({
        type: 'POST',
        url: '/carts/create_cart/',
        data: {
          dish: String(dish),
          user: String(user),
          quantity: String(num), 
          csrfmiddlewaretoken: csrfmiddlewaretoken
        },
      });
    });
  });

$(document).ready(function() {
  $('.CartBlockCounterMinus').click(function(e) {
    e.preventDefault();
    var csrfmiddlewaretoken = $(this).siblings('input[name="csrfmiddlewaretoken"]').val();
    var user = String($(this).siblings('input[name="user"]').val());
    var dish = String($(this).siblings('input[name="dish"]').val());
    var cart_pk = String($(this).siblings('input[name="cart_pk"]').val());
    var num = String($(this).siblings('input[name="num"]').val());
    var quantity = String($('.CartBlockCounterQuantity_' + dish).text())

    if (quantity == "1") {
      $.ajax({
        type: 'POST',
        url: '/carts/delete_cart/',
        data: {
            user: String(user),
            pk: String(cart_pk),
            csrfmiddlewaretoken: csrfmiddlewaretoken
        },
        success: function(response) {
            $('.CartBlockWrapper_' + dish).remove();
        },
        error: function(xhr, errmsg, err) {
            console.log("error" + errmsg);
        }
      });
    } else {
      $.ajax({
        type: 'POST',
        url: '/carts/create_cart/',
        data: {
            dish: String(dish),
            user: String(user),
            quantity: String(num),
            csrfmiddlewaretoken: csrfmiddlewaretoken
        },
        success: function(response) {
            $('.CartBlockCounterQuantity_' + response.dish).text(response.get_quantity); 
            $('.CartBlockCounterPrice_' + response.dish).text(response.total_price + " сум");
            $('.TextTotalPriceP').text("К оплате " + response.total_price_all_cart_user + " сум"); 
        },
        error: function(xhr, errmsg, err) {
            console.log("error" + errmsg);
        }
      });
    }
  });
});

$(document).ready(function() {
  $('.CartBlockCounterPlus').click(function(e) {
      e.preventDefault();
      var csrfmiddlewaretoken = $(this).siblings('input[name="csrfmiddlewaretoken"]').val();
      var user = String($(this).siblings('input[name="user"]').val());
      var dish = String($(this).siblings('input[name="dish"]').val());
      var num = String($(this).siblings('input[name="num"]').val());

      $.ajax({
          type: 'POST',
          url: '/carts/create_cart/',
          data: {
              dish: String(dish),
              user: String(user),
              quantity: String(num),
              csrfmiddlewaretoken: csrfmiddlewaretoken
          },
          success: function(response) {
              $('.CartBlockCounterQuantity_' + response.dish).text(response.get_quantity); 
              $('.CartBlockCounterPrice_' + response.dish).text(response.total_price + " сум");
              $('.TextTotalPriceP').text("К оплате " + response.total_price_all_cart_user + " сум"); 
          },
          error: function(xhr, errmsg, err) {
              console.log("error" + errmsg);
          }
      });
  });
});


