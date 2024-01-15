document.addEventListener("DOMContentLoaded", function() {
    const registrationForm = document.getElementById("registrationForm");
    const categoriesDiv = document.getElementById("categories");
    const addToCartForm = document.getElementById("addToCartForm");
    const foodItemSelect = document.getElementById("foodItem");
    const tablesDiv = document.getElementById("tables");
    const paymentForm = document.getElementById("paymentForm");
  
    registrationForm.addEventListener("submit", function(event) {
      event.preventDefault();
      const username = document.getElementById("username").value;
      const name = document.getElementById("name").value;
      const surname = document.getElementById("surname").value;
      const phone = document.getElementById("phone").value;
  
      fetch('http://localhost:8000/users/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, name: name, surname: surname, phone: phone })
      })
      .then(response => response.json())
      .then(data => {
      })
      .catch(error => {
        console.error('Ошибка регистрации:', error);
      });
    });
  
    fetch('http://localhost:8000/users/categories')
      .then(response => response.json())
      .then(data => {
      })
      .catch(error => {
        console.error('Ошибка получения категорий:', error);
    });

    // addToCartForm.addEventListener("submit", function(event) {
    //   event.preventDefault();
    //   const foodItem = foodItemSelect.value;
  
    //   fetch('http://localhost:8000/api/add_to_cart', {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({ foodItem: foodItem })
    //   })
    //   .then(response => response.json())
    //   .then(data => {
    //   })
    //   .catch(error => {
    //     console.error('Error adding to cart:', error);
    //   });
    // });
  
    // fetch('http://localhost:8000/api/tables')
    //   .then(response => response.json())
    //   .then(data => {
    //   })
    //   .catch(error => {
    //     console.error('Error fetching tables:', error);
    //   });
  
    // paymentForm.addEventListener("submit", function(event) {
    //   event.preventDefault();
    //   const paymentAmount = document.getElementById("paymentAmount").value;
  
    //   fetch('http://localhost:8000/api/make_payment', {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({ amount: paymentAmount })
    //   })
    //   .then(response => response.json())
    //   .then(data => {
    //   })
    //   .catch(error => {
    //     console.error('Error making payment:', error);
    //   });
    // });
  });