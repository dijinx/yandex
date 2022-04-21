# Функция принимает 4 аргумента:
#     1. distance - расстояние в метрах
#     2. big_size_shipment - габариты груза   - boolean
#     3. fragility - хрупкость груза          - boolean
#     4. delivery_service_load- коэффициент загрузки сервиса доставки - float


def delivery_price(distance, big_size_shipment, fragility, delivery_service_load):
    min_delivery_price = 0
    distance_price = 100
    big_size_prise_true = 200
    fragility_true_prise, fragility_possible_distance = 300, 30000

    if fragility and distance > fragility_possible_distance:
        quit('Доставка хрупкого груза на расстояние больше 30км запрещена!')
    # print(f'Сумма доставки {min_delivery_price}')
    if 1 < distance <= 2000:
        min_delivery_price += 50
        print('Нет надбавки за расстояние')
    if 2001 <= distance <= 10000:
        min_delivery_price += distance_price
        print(f'Надбавка за расстояние {distance}м {distance_price} руб.')
    if 10001 <= distance <= 30000:
        min_delivery_price += distance_price * 2
        print(f'Надбавка за расстояние {distance}м {distance_price * 2} руб.')
    if 30001 <= distance:
        min_delivery_price += distance_price * 3
        print(f'Надбавка за расстояние {distance}м {distance_price * 3} руб.')
    if big_size_shipment:
        min_delivery_price += big_size_prise_true
        print(f'Надбавка за большой габарит груза {big_size_prise_true} руб.')
    if fragility:
        min_delivery_price += fragility_true_prise
        print(f'Надбавка за хрупкость груза {fragility_true_prise}')
    if min_delivery_price < 400:
        min_delivery_price = 400

    pre_last_price = min_delivery_price

    min_delivery_price *= delivery_service_load

    print(f'Коэффициент загруженности службы доставки {pre_last_price} * {delivery_service_load}')
    print(f'Общая стоимость доставки {min_delivery_price} руб.')
    return min_delivery_price


delivery_price(2001, True, True, 1.4)
