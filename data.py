# Файл с данными для тестов, включая сообщения об ошибках и примеры заказов
class CourierMessages:
    NOT_ENOUGH_DATA = "Недостаточно данных для создания учетной записи"
    LOGIN_ALREADY_IN_USE = "Этот логин уже используется. Попробуйте другой."
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    NOT_ENOUGH_DATA_FOR_LOGIN = "Недостаточно данных для входа"
    INVALID_LOGIN_OR_PASSWORD = "Учетная запись не найдена"

class OrderData:
    order_data_1 = {
        'firstName': 'Елена',
        'lastName': 'Иванова',
        'address': 'Ленина 12',
        'metroStation': 5,
        'phone': '+79261112233',
        'rentTime': 2,
        'deliveryDate': '2025-05-17',
        'comment': 'Кататься с друзьями!',
        'color': ['GREY']
    }
    order_data_2 = {
        'firstName': 'Дмитрий',
        'lastName': 'Петров',
        'address': 'Советская 45',
        'metroStation': 6,
        'phone': '+79262223344',
        'rentTime': 3,
        'deliveryDate': '2025-05-18',
        'comment': 'Нужен быстрый самокат',
        'color': ['BLACK']
    }
    order_data_3 = {
        'firstName': 'Ольга',
        'lastName': 'Сидорова',
        'address': 'Гагарина 78',
        'metroStation': 7,
        'phone': '+79263334455',
        'rentTime': 4,
        'deliveryDate': '2025-05-19',
        'comment': 'Любой цвет подойдёт',
        'color': ['BLACK', 'GREY']
    }
    order_data_4 = {
        'firstName': 'Алексей',
        'lastName': 'Козлов',
        'address': 'Мичурина 91',
        'metroStation': 8,
        'phone': '+79264445566',
        'rentTime': 5,
        'deliveryDate': '2025-05-20',
        'comment': 'Без цвета, главное доставить',
        'color': []
    }