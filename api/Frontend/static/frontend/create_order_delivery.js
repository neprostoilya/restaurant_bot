jQuery(document).ready(function($) {

  $('.ButtonWrapperAtable').on('click', function(e) {
    e.preventDefault();

    const tg = Telegram.WebApp;

    var userData;

    function GetUser(callback) {
      fetch("https://cafe-family-7a.tw1.su/users/users/" + tg.initDataUnsafe.user.id  + "/")
        .then(response => response.json())
        .then(data => {
          userData = data;
          callback(userData);
        })
        .catch(err => {
          tg.showPopup({
              title: "Ошибка",
              message: `Вы не зарегистрированы в системе!`,
              buttons: [{
                type: "destructive",
                text: "Закрыть"
              }],
            },
            callback
          );
        });
    }

    GetUser(function(userData) {
      processData(userData);
    });

    function processData(userData) {
      var userData = JSON.parse(JSON.stringify(userData));

      var userPk = userData[0].pk

      var userPhone = userData[0].phone

      var username = userData[0].username

      var userTelegramId = userData[0].telegram_pk

      var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

      var dishes = [];

      var position = JSON.parse(localStorage.getItem('lastMarker')).position

      const latitude = position[0]; // Широта

      const longitude = position[1]; // Долгота
      
      var text_dishes = '';
 
      cartItems.forEach(function(item, i) {
        dishes.push(item.dish_pk)
        text_dishes += `<b>Блюдо</b> <code>#${i+1}</code>\n<b>Название:</b> <code>${item.title}</code>\n<b>Колл-во:</b> <code>${item.quantity}</code>\n<b>Цена:</b> <code>${item.total_price}</code> <b>сум</b>\n\n`;
      });

      fetch("https://cafe-family-7a.tw1.su/orders/create_order/", {
          method: "POST",
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            user: userPk,
            type_order: 'Доставка',
            latitude: latitude,
            longitude: longitude,
            status: 'Ожидание'
          })
        })
        .then(response => response.json())
        .then(data => {
          var order = data;

          var total_price_all_dishes = 0;
          var total_quantity_all_dishes = 0;

          cartItems.forEach(function(item, i) {
            total_price_all_dishes += item.total_price
            total_quantity_all_dishes += item.quantity
            createDishOrder(order.pk, item.dish_pk, item.total_price, item.quantity);
          });

          const date = new Date(data.datetime_created);

          const formattedDateTime = `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')} ${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')};`
          sendTelegramOrderNotification(formattedDateTime, userPhone, username, userTelegramId, order, order.pk,
           total_price_all_dishes, total_quantity_all_dishes, text_dishes)
        });


      function createDishOrder(order_id, dish_pk, total_price, total_quantity) {
        fetch("https://cafe-family-7a.tw1.su/orders/create_dish_order/", {
          method: "POST",
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            dish: dish_pk,
            order: order_id,
            total_price: total_price,
            total_quantity: total_quantity
          })
        });

      };

      function sendTelegramOrderNotification(datetimeCreated, userPhone, username, userTelegramId,
        order, order_pk, total_price_all_dishes, total_quantity_all_dishes, text_dishes) {
        var text = `
<b>Заказ</b> <code>#${order_pk}</code>

<b>Тип заказа:</b> <code>Доставка</code>

<b>От Пользователя:</b> <code>@${username}</code>

<b>Номер:</b> <code>${userPhone}</code>

<b>Дата и время создания:</b>   
<code>${datetimeCreated}</code>


${text_dishes}
<b>Общая цена:</b> <code>${total_price_all_dishes}</code> <b>сум</b> 

<b>Общее колл-во:</b> <code>${total_quantity_all_dishes}</code>`;

        var token_1 = '6898947200:AAGcnJRBEw2E_I0p4Mey4jcMXNJSGML3s_g';
        var token_2 = '7184297327:AAFs3jwkVV8gXXvDSRMtLkgZmPRCx6KcYL0';
        console.log(order);
        var buttons = JSON.stringify({
          inline_keyboard: [
            [{
                text: '✔️ Принять',
                callback_data: `accept_order_${order_pk}_${userTelegramId} `
              },
              {
                text: '✖️ Отклонить',
                callback_data: `reject_order_${order_pk}_${userTelegramId} `
              }
            ]
          ]
        });

        fetch("https://cafe-family-7a.tw1.su/users/get_managers/")
          .then(response => response.json())
          .then(data => {
            data.forEach(userManager => {
              var chatIdManager = userManager.telegram_pk;
              sendMessageToManager(chatIdManager, token_2, buttons, text, latitude, longitude);
            });
          });
        sendMessageToUser(token_1, userTelegramId);
      };

      function sendMessageToUser(token_1, userTelegramId) {
        fetch("https://api.telegram.org/bot" + token_1 + "/sendMessage", {
            method: "POST",
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              chat_id: userTelegramId,
              text: 'Отлично, заявка создана, ждите одобрение от мененджера.😊',
              parse_mode: 'HTML'
            })
          })
          .then(response => {
            const tg = Telegram.WebApp;
            localStorage.clear();
            tg.close()
          });
      };

      function sendMessageToManager(chatIdManager, token, buttons, text, latitude, longitude) {
        fetch("https://api.telegram.org/bot" + token + "/sendLocation", {
    method: "POST",
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        chat_id: chatIdManager,
        latitude: latitude,
        longitude: longitude,
        parse_mode: 'HTML'
    })
})
.then(response => response.json()) 
.then(data => {
    console.log("Location sent response:", data); 
    fetch("https://api.telegram.org/bot" + token + "/sendMessage", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            chat_id: chatIdManager, 
            text: text,
            reply_markup: buttons,
            parse_mode: 'HTML'
        })
    })
   .then(response => response.json())
   .then(data => {
        console.log("Message sent response:", data); 
    })
   .catch(error => {
        console.error("Error sending message:", error);
    });
})
.catch(error => {
    console.error("Error sending location:", error);
});
      }
    }
  });
});