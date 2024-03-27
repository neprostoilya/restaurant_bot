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

        // let tg = window.Telegram.WebApp;

        var user = $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/users/users/" + '5974014808/',
            data: {
            },
            success: function(response) {
                var user = response.data;
            },
            error: function(err) {
                var user = 'None';
            }
        });

        console.log(user.responseJSON)

        var cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

        var total_price_all_dishes = 0;

        var total_quantity_all_dishes = 0;

        var dishes = [];
        
        var text_dishes = '';

        cartItems.forEach(function(item, i) {
          dishes.push(item.dish_pk)
          text_dishes += `Блюдо №${i+1}\nНазвание: ${item.title},\nКолл-во: ${item.quantity}, Цена: ${item.total_price} сум\n\n`;
          total_price_all_dishes += item.total_price;
          total_quantity_all_dishes += item.quantity;
        });

        var storedPeopleCount = localStorage.getItem('selectedPeopleCount');

        var storedTable = localStorage.getItem('selectedTable');

        var storedTime = localStorage.getItem('selectedTime');
        
        var order = $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/orders/create_order/",
            data: {
                user: user.pk,
                dishes: dishes,
                table: storedTable,
                people_quantity: storedPeopleCount,
                total_price: total_price_all_dishes, 
                total_quantity: total_quantity_all_dishes,
                datetime_selected: storedTime + ':00',
                status: 'Ожидание'
            },
            success: function(response) {
                var order = response.data;
            },
            error: function(err) {
                var order = 'None';
            }
        });

       

        var text = `
Заказ №${order.id}

От @кто то

Номер: +999999999

Забронированное время: ${storedTime}


${text_dishes}
Номер столика: ${storedTable}

Колл-во людей: ${storedPeopleCount}

Общая цена: ${total_price_all_dishes} сум

Общее колл-во: ${total_quantity_all_dishes}`;

        var chatid = '-4112391046';
        var token = '6898947200:AAGcnJRBEw2E_I0p4Mey4jcMXNJSGML3s_g';
        
        var buttons = JSON.stringify({
            inline_keyboard: [
                [
                    { text: '✔️ Принять', callback_data: `accept_order_${order.id}_${chatid}` },
                    { text: '✖️ Отклонить', callback_data: `reject_orde_${order.id}_${chatid}` }
                ]
            ]
        });
    
        $.ajax({
            type: "POST",
            url: "https://api.telegram.org/bot" + token + "/sendMessage",
            data: {
                chat_id: chatid,
                text: text,
                reply_markup: buttons,
                parse_mode: 'HTML'
            },
            success: function(response) {
                console.log('Message sent successfully!');
                // tg.close()
            },
            error: function(err) {
                console.error('Error sending message:', err);
                // tg.close()
            }
        });
    });
});
