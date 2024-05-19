jQuery(document).ready(function($) {
    $('#typeNumber').on('input', function() {
        var peopleCount = $(this).val();
        localStorage.setItem('selectedPeopleCount', peopleCount);
    });
    
    var storedPeopleCount = localStorage.getItem('selectedPeopleCount');
    
    if (storedPeopleCount) {
        $('#typeNumber').val(storedPeopleCount);
    }
    
    $('.ButtonWrapperAtable').on('click', function(e) {
        e.preventDefault();
  
        const tg = Telegram.WebApp;
  
        var userData; 
  
        function GetUser(callback) {
            fetch("http://cafe-family-7a.tw1.su/users/users/" + tg.initDataUnsafe.user.id   + "/")
                .then(response => response.json())
                .then(data => {
                    userData = data; 
                    callback(userData); 
                })
                .catch(err => {
                    tg.showPopup(
                    {
                        title: "Ошибка", 
                        message: `Вы не зарегистрированы в системе!`,
                        buttons: [{ type: "destructive", text: "Закрыть" }],  
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
  
            var username= userData[0].username
  
            var userTelegramId= userData[0].telegram_pk
  
            var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
  
            var dishes = [];
            
            var text_dishes = '';
  
            cartItems.forEach(function(item, i) {
                dishes.push(item.dish_pk)
                text_dishes += `<b>Блюдо</b> <code>#${i+1}</code>\n<b>Название:</b> <code>${item.title}</code>\n<b>Колл-во:</b> <code>${item.quantity}</code>\n<b>Цена:</b> <code>${item.total_price}</code> <b>сум</b>\n\n`;
            });
  
            var storedPeopleCount = localStorage.getItem('selectedPeopleCount');
  
            var selectedPlaceName = localStorage.getItem('selectedPlaceName');
  
            var storedTime = localStorage.getItem('selectedTime');
            
            fetch("http://cafe-family-7a.tw1.su/orders/create_order/", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user: userPk,
                    type_order: 'Бронирование',
                    place: selectedPlaceName,
                    people_quantity: storedPeopleCount,
                    datetime_selected: storedTime + ':00',
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
                sendTelegramOrderNotification(formattedDateTime, userPhone, username, userTelegramId, order, storedTime, order.pk,
                    selectedPlaceName, storedPeopleCount, total_price_all_dishes, total_quantity_all_dishes, text_dishes)
            });
            
  
            function createDishOrder(order_id, dish_pk, total_price, total_quantity) {
                fetch("http://cafe-family-7a.tw1.su/orders/create_dish_order/", {
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
                order, storedTime, order_pk, selectedPlaceName, storedPeopleCount, total_price_all_dishes, total_quantity_all_dishes, text_dishes) {
                var text = `
<b>Заказ</b> <code>#${order_pk}</code>

<b>От Пользователя:</b> <code>@${username}</code>

<b>Номер:</b> <code>${userPhone}</code>

<b>Дата и время создания:</b>   
<code>${datetimeCreated}</code>

<b>Забронированное время:</b> <code>${storedTime}</code>


${text_dishes}
<b>Место:</b> <code>${selectedPlaceName}</code>

<b>Колл-во людей:</b> <code>${storedPeopleCount}</code>

<b>Общая цена:</b> <code>${total_price_all_dishes}</code> <b>сум</b> 

<b>Общее колл-во:</b> <code>${total_quantity_all_dishes}</code>`;
                
                var token_1 = '6513329874:AAH-ufpn6xB55o8J8eyi2dPfVXMlxGWiMAU';
                var token_2 = '7184297327:AAFs3jwkVV8gXXvDSRMtLkgZmPRCx6KcYL0';
                console.log(order_pk, order);
                var buttons = JSON.stringify({
                    inline_keyboard: [
                        [
                            { text: '✔️ Принять', callback_data: `accept_order_${order_pk}_${userTelegramId} `},
                            { text: '✖️ Отклонить', callback_data: `reject_order_${order_pk}_${userTelegramId} `}
                        ]
                    ]
                });
  
                fetch("http://cafe-family-7a.tw1.su/users/get_managers/")
                .then(response => response.json())
                .then(data => {
                    data.forEach(userManager => { 
                        var chatIdManager = userManager.telegram_pk; 
                        sendMessageToManager(chatIdManager, token_2, buttons, text);
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
  
            function sendMessageToManager(chatIdManager, token_2, buttons, text) {
              fetch("https://api.telegram.org/bot" + token_2 + "/sendMessage", {
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
              });
          }
        }
    });
  });
  