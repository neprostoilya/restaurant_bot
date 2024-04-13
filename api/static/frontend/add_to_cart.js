$(document).ready(function() {
  function addToCart(dish) {
      var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

      var existingItem = cartItems.find(function(item) {
        return item.dish_pk === dish.dish_pk;
      });
      
      if (existingItem) {
        existingItem.quantity++;
        existingItem.total_price = existingItem.quantity * existingItem.price;
      } else {
        dish.quantity = 1;
        cartItems.push(dish);
      }    

      localStorage.setItem('cartItems', JSON.stringify(cartItems));
      displayCartItems();
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
      "price": price,
      "total_price": price,
    };
    
    addToCart(dish); 
  });

  $('.price-p').text((i, text) => {
    const [ price, currency ] = text.split(' ');
    return `${(+price).toLocaleString()} ${currency}`;
  });

  $('.modal-price').text((i, text) => {
    const [ price, currency ] = text.split(' ');
    return `${(+price).toLocaleString()} ${currency}`;
  });

});


