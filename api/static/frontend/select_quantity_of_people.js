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
            $.ajax({
                type: "GET",
                url: "https://1c01-95-46-67-138.ngrok-free.app/users/users/" + tg.initDataUnsafe.user.id + "/",
                success: function(data) {
                    userData = data; 
                    callback(userData); 
                },
                error: function(err) {
                    tg.showPopup(
                    {
                        title: "Ошибка", 
                        message: "Вы не зарегистрированы в системе!",
                        buttons: [{ type: "destructive", text: "Закрыть" }], // Optional
                    },
                    callback
                    );
                }
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

            var total_price_all_dishes = 0;

            var total_quantity_all_dishes = 0;

            var dishes = [];
            
            var text_dishes = '';

            cartItems.forEach(function(item, i) {
                dishes.push(item.dish_pk)
                text_dishes += `<b>Блюдо</b> <code>#${i+1}</code>\n<b>Название:</b> <code>${item.title}</code>\n<b>Колл-во:</b> <code>${item.quantity}</code>\n<b>Цена:</b> <code>${item.total_price}</code> <b>сум</b>\n\n`;
                total_price_all_dishes += item.total_price;
                total_quantity_all_dishes += item.quantity;
            });

            var storedPeopleCount = localStorage.getItem('selectedPeopleCount');

            var storedTable = localStorage.getItem('selectedTable');

            var storedTime = localStorage.getItem('selectedTime');
            
            localStorage.clear();

            $.ajax({
                type: "POST",
                url: "https://1c01-95-46-67-138.ngrok-free.app/orders/create_order/",
                data: JSON.stringify({
                    user: userPk,
                    table: storedTable,
                    people_quantity: storedPeopleCount,
                    total_price: total_price_all_dishes, 
                    total_quantity: total_quantity_all_dishes,
                    dishes: dishes, 
                    datetime_selected: storedTime + ':00',
                    status: 'Ожидание'
                }),
                contentType: 'application/json', 
                success: function(data) {
                    var order = data;

                    const date = new Date(data.datetime_created);

                    const formattedDateTime = `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')} ${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')};`

                    sendTelegramOrderNotification(formattedDateTime, userPhone, username, userTelegramId, order, storedTime,
                         storedTable, storedPeopleCount, total_price_all_dishes, total_quantity_all_dishes, text_dishes);
                },
                error: function(err) {
                    var order = 'None';
                }
            });
            
        
            function sendTelegramOrderNotification(datetimeCreated, userPhone, username, userTelegramId, 
                order, storedTime, storedTable, storedPeopleCount, total_price_all_dishes, total_quantity_all_dishes, text_dishes) {
                var text = `
<b>Заказ</b> <code>#${order.id}</code>

<b>От Пользователя:</b> <code>@${username}</code>

<b>Номер:</b> <code>${userPhone}</code>

<b>Дата и время создания:</b>   
<code>${datetimeCreated}</code>

<b>Забронированное время:</b> <code>${storedTime}</code>


${text_dishes}
<b>Номер столика:</b> <code>${storedTable}</code>

<b>Колл-во людей:</b> <code>${storedPeopleCount}</code>

<b>Общая цена:</b> <code>${total_price_all_dishes}</code> <b>сум</b> 

<b>Общее колл-во:</b> <code>${total_quantity_all_dishes}</code>`;
                
                var chatid = '5974014808';
                var token_1 = '6898947200:AAGcnJRBEw2E_I0p4Mey4jcMXNJSGML3s_g';
                var token_2 = '7174377582:AAG2bot7iwpYE8DNVSC6sivYCdhyyMXz6jU';
                
                var buttons = JSON.stringify({
                    inline_keyboard: [
                        [
                            { text: '✔️ Принять', callback_data: `accept_order_${order.id}_${userTelegramId} `},
                            { text: '✖️ Отклонить', callback_data: `reject_order_${order.id}_${userTelegramId} `}
                        ]
                    ]
                });
                
                $.ajax({
                    type: "POST",
                    url: "https://api.telegram.org/bot" + token_2 + "/sendMessage",
                    data: {
                        chat_id: chatid,
                        text: text,
                        reply_markup: buttons,
                        parse_mode: 'HTML'
                    },
                    success: function(response) {
                        console.log('Message sent to manager successfully!');
                    },
                });
                
                $.ajax({
                    type: "POST",
                    url: "https://api.telegram.org/bot" + token_1 + "/sendMessage",
                    data: {
                        chat_id: userTelegramId,
                        text: 'Отлично, заявка создана, ждите одобрение от мененджера.😊',
                        parse_mode: 'HTML'
                    },
                    success: function(response) {
                        const tg = Telegram.WebApp;
                        tg.close()
                    }
                });
            }
        }
    });
});