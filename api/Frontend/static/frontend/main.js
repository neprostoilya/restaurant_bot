$(document).ready(function() {
  function addToCart(dish) {
      var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

      var existingItem = cartItems.find(function(item) {
        return item.dish_pk === dish.dish_pk;
      });

      if (existingItem) {
        existingItem.quantity++;
        existingItem.total_price = existingItem.quantity * existingItem.total_price;
      } else {
        dish.quantity = 1;
        cartItems.push(dish);
      }    

      localStorage.setItem('cartItems', JSON.stringify(cartItems));

      displayCartItems();
  }

  function plusToCart(dish) {
    var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

    var existingItem = cartItems.find(function(item) {
      return item.dish_pk == dish.dish_pk;
    });
    alert(existingItem)
    existingItem.quantity++;
    existingItem.total_price = existingItem.quantity * existingItem.total_price;

    localStorage.setItem('cartItems', JSON.stringify(cartItems));

    displayCartItems();
  }

  function minusToCart(dish) {
    var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

    var existingItem = cartItems.find(function(item) {
      return item.dish_pk == dish.dish_pk;
    });
    alert(existingItem)

    existingItem.quantity--;
    existingItem.total_price = existingItem.quantity * existingItem.total_price;

    localStorage.setItem('cartItems', JSON.stringify(cartItems));

    displayCartItems();
  }

  function displayCartItems() {
      var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

      var cartItemsList = $('#cartItemsList');

      cartItemsList.empty();

      cartItems.forEach(function(item) {

        var cartBlockWrapper = $('<div>').addClass('CartBlockWrapper_' + item.dish);

        var cartBlockInfo = $('<div>').addClass('CartBlockInfo');

        var cartBlockImg = $('<div>').addClass('CartBlockImg');
        
        var img = $('<img>').attr('src', item.image).css({ 'width': '90px', 'height': '90px' });

        cartBlockImg.append(img);
        
        var cartBlockTitle = $('<h3>').addClass('CartBlockTitle').text(item.title);
    
        var cartBlockCounterWrapper = $('<div>').addClass('CartBlockCounterWrapper');
        var cartBlockCounter = $('<div>').addClass('CartBlockCounter').css({ 'margin': '0px 0px 8px' });
        
        var hiddenInputsMinus = $('<div>');

        hiddenInputsMinus.append(
          $('<input>').attr('type', 'hidden').attr('name', 'dish_pk').val(item.dish_pk),
          $('<a>').attr('type', 'submit').addClass('CartBlockCounterMinus').append($('<span>').append($('<i>').addClass('fa-solid fa-minus')))
        );

        var quantity = $('<p>').addClass('CartBlockCounterQuantity_' + item.dish).text(item.quantity);

        var hiddenInputsPlus = $('<div>');

        hiddenInputsPlus.append(
          $('<input>').attr('type', 'hidden').attr('name', 'dish_pk').val(item.dish_pk),
          $('<a>').attr('type', 'submit').addClass('CartBlockCounterPlus').append($('<span>').append($('<i>').addClass('fa-solid fa-plus')))
        );
        
        var counterPrice = $('<p>').addClass('CartBlockCounterPrice_' + item.dish).text(item.total_price + ' сум');
    
        cartBlockCounter.append(hiddenInputsMinus, quantity, hiddenInputsPlus);

        cartBlockCounterWrapper.append(cartBlockCounter, counterPrice);
    
        cartBlockInfo.append(cartBlockImg, cartBlockTitle);

        cartBlockWrapper.append(cartBlockInfo, cartBlockCounterWrapper);
    
        cartItemsList.append(cartBlockWrapper);
    });      
  }

  $('.add-to-cart-button').on('click', function(e) {

    var parentForm = $(this).closest('form');

    var dish_pk = Number(parentForm.find('input[name="dish_pk"]').val());

    var image = String(parentForm.find('input[name="image"]').val());

    var title = String(parentForm.find('input[name="title"]').val());

    var description = String(parentForm.find('input[name="description"]').val());

    var price = Number(parentForm.find('input[name="price"]').val());

    var category = Number(parentForm.find('input[name="category"]').val());

    var dish = {
      "dish_pk": dish_pk, 
      "image": image, 
      "title": title, 
      "description": description, 
      "category": category, 
      "quantity": 1,
      "total_price": price,
      };
    
    addToCart(dish); 
});

$('.CartBlockCounterPlus').on('click', function(e) {

  var parentForm = $(this).closest('form');

  var dish_pk = Number(parentForm.find('input[name="dish_pk"]').val());

  var image = String(parentForm.find('input[name="image"]').val());

  var title = String(parentForm.find('input[name="title"]').val());

  var description = String(parentForm.find('input[name="description"]').val());

  var price = Number(parentForm.find('input[name="price"]').val());

  var category = Number(parentForm.find('input[name="category"]').val());

  var dish = {
    "dish_pk": dish_pk, 
    "image": image, 
    "title": title, 
    "description": description, 
    "category": category, 
    "quantity": 1,
    "total_price": price,
    };
  
  plusToCart(dish); 
  console.log('ss')
});

$('.CartBlockCounterMinus').on('click', function(e) {

  var parentForm = $(this).closest('form');

  var dish_pk = Number(parentForm.find('input[name="dish_pk"]').val());

  var image = String(parentForm.find('input[name="image"]').val());

  var title = String(parentForm.find('input[name="title"]').val());

  var description = String(parentForm.find('input[name="description"]').val());

  var price = Number(parentForm.find('input[name="price"]').val());

  var category = Number(parentForm.find('input[name="category"]').val());

  var dish = {
    "dish_pk": dish_pk, 
    "image": image, 
    "title": title, 
    "description": description, 
    "category": category, 
    "quantity": 1,
    "total_price": price,
  };
  console.log('ss')
  minusToCart(dish); 
});

  displayCartItems();
});
