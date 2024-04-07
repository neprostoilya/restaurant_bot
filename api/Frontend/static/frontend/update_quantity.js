$(document).ready(function() {  
  function displayCartItems() {
      var cartItems = JSON.parse(localStorage.getItem('cartItems')) || NaN;
    
      if (cartItems) {
        var cartItemsList = $('#cartItemsList');

        var total_price_all_dishes = 0;
  
        cartItemsList.empty();
  
        cartItems.forEach(function(item) {
  
          total_price_all_dishes += item.total_price;
  
          var cartBlockWrapper = $('<div>').addClass('CartBlockWrapper_' + item.dish);
  
          var cartBlockInfo = $('<div>').addClass('CartBlockInfo');
  
          var cartBlockImg = $('<div>').addClass('CartBlockImg');
          
          var img = $('<img>').attr('src', item.image).css({ 'width': '90px', 'height': '90px' });
  
          cartBlockImg.append(img);
          
          var cartBlockTitle = $('<h3>').addClass('CartBlockTitle').text(item.title);
      
          var cartBlockCounterWrapper = $('<div>').addClass('CartBlockCounterWrapper');
          var cartBlockCounter = $('<div>').addClass('CartBlockCounter').css({ 'margin': '0px 0px 8px' });
          
          var hiddenInputsMinus = $('<form>').addClass('cart-form-minus');
  
          hiddenInputsMinus.append(
            $('<input>').attr('type', 'hidden').attr('name', 'dish_pk').val(item.dish_pk),
            $('<input>').attr('type', 'hidden').attr('name', 'quantity').val(item.quantity),
            $('<input>').attr('type', 'hidden').attr('name', 'price').val(item.price),
            $('<button>').addClass('minus-to-cart-button').append($('<span>').append($('<i>').addClass('fa-solid fa-minus')))
          );
  
          var quantity = $('<p>').addClass('CartBlockCounterQuantity_' + item.dish_pk).text(item.quantity);
  
          var hiddenInputsPlus = $('<form>').addClass('cart-form-plus');
  
          hiddenInputsPlus.append(
            $('<input>').attr('type', 'hidden').attr('name', 'dish_pk').val(item.dish_pk),
            $('<input>').attr('type', 'hidden').attr('name', 'quantity').val(item.quantity),
            $('<input>').attr('type', 'hidden').attr('name', 'price').val(item.price),
            $('<button>').addClass('plus-to-cart-button').append($('<span>').append($('<i>').addClass('fa-solid fa-plus')))
          );
          
          var counterPrice = $('<p>').addClass('CartBlockCounterPrice_' + item.dish_pk).text(item.total_price + ' сум');
      
          cartBlockCounter.append(hiddenInputsMinus, quantity, hiddenInputsPlus);
  
          cartBlockCounterWrapper.append(cartBlockCounter, counterPrice);
      
          cartBlockInfo.append(cartBlockImg, cartBlockTitle);
  
          cartBlockWrapper.append(cartBlockInfo, cartBlockCounterWrapper);
      
          cartItemsList.append(cartBlockWrapper);
        });     
    
        $('.TextTotalPriceP').text('К оплате ' + total_price_all_dishes + ' сум');
      } else {
        console.log('#DD');
      }
  }

  displayCartItems();

  function updateCartItem(dish, action) {
    var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

    var existingItem = cartItems.find(function(item) {
      return item.dish_pk === dish.dish_pk;
    });
    
    if (action === 'plus') {
        existingItem.quantity++;
    } else if (action === 'minus') {
        existingItem.quantity--;
    }

    if (existingItem.quantity > 0) {

      total_price = existingItem.quantity * existingItem.price;

      $('input[name="quantity"]').val(existingItem.quantity);

      $('.CartBlockCounterQuantity_' + existingItem.dish_pk).text(existingItem.quantity);

      $('.CartBlockCounterPrice_' + existingItem.dish_pk).text(total_price + ' сум');

      existingItem.total_price = total_price


      localStorage.setItem('cartItems', JSON.stringify(cartItems));

      var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

      var total_price_all_dishes = 0;

      cartItems.forEach(function(item) {
        total_price_all_dishes += item.total_price;
      });
      
      $('.TextTotalPriceP').text('К оплате ' + total_price_all_dishes + ' сум');

    } else {
      cartItems = cartItems.filter(item => item.dish_pk !== existingItem.dish_pk);
      localStorage.setItem('cartItems', JSON.stringify(cartItems));
      displayCartItems();
    }
  }

  $('.plus-to-cart-button').on('click', function(e) {
    e.preventDefault();
    var parentForm = $(this).closest('form');

    var dish_pk = Number(parentForm.find('input[name="dish_pk"]').val());

    var quantity = String(parentForm.find('input[name="quantity"]').val());

    var price = Number(parentForm.find('input[name="price"]').val());

    var dish = {
      "dish_pk": dish_pk, 
      "quantity": quantity,
      "price": price,
    };

    updateCartItem(dish, 'plus');
  });

  $('.minus-to-cart-button').on('click', function(e) {
    e.preventDefault();
    var parentForm = $(this).closest('form');

    var dish_pk = Number(parentForm.find('input[name="dish_pk"]').val());

    var quantity = String(parentForm.find('input[name="quantity"]').val());

    var price = Number(parentForm.find('input[name="price"]').val());

    var dish = {
      "dish_pk": dish_pk, 
      "quantity": quantity,
      "price": price,
    };

    updateCartItem(dish, 'minus');

  });
});
