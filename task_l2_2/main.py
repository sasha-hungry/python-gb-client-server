"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": [
        {
            "item": "принтер", (возможные проблемы с кирилицей)
            "quantity": "10",
            "price": "6700",
            "buyer": "Ivanov I.I.",
            "date": "24.09.2017"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        }
    ]
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json

def write_order_to_json(item, quantity, price, buyer, date):
    """ запись данных в json"""
    
    with open('orders.json','r', encoding='utf-8') as output_file:
        data = json.load(output_file)
    
    with open('orders.json', 'w', encoding='utf-8') as input_file:
        orders_list = data['orders']
        order_info = {'item': item, 'quantity': quantity,'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_info)
        json.dump(data, input_file, indent=4, ensure_ascii=False)
        

write_order_to_json('printer', '10', '6700', 'Ivanov K.S.', '24.09.2017')
write_order_to_json('scaner', '20', '10000', 'Petrov P.P.', '11.01.2018')
write_order_to_json('scaner', '20', '10000', 'Petrov P.P.', '11.01.2018') 
write_order_to_json('scaner', '20', '10000', 'Petrov P.P.', '11.01.2018')        
