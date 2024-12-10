# Модель пользователя
class User:
    def __init__(self, name, age, pin, is_admin=False):
        self.name = name
        self.age = age
        self.pin = pin
        self.is_admin = is_admin
        self.orders = []  # Список заказов пользователя

    def add_order(self, order_name, price_rub):
        # Добавляем заказ с ценой в рублях
        order = {
            'название': order_name,
            'цена': price_rub,
            'цена_доллары': price_rub / 75  # Примерный курс 1 доллар = 75 рублей
        }
        self.orders.append(order)


# Список пользователей (вместо базы данных)
users = []

# Регистрация админа
admin_user = User("admin", 30, "admin123", is_admin=True)
users.append(admin_user)

# Пример добавления заказов для тестирования
user1 = User("Иван", 25, "ivan123")
user1.add_order("Пицца", 1500)  # 1500 рублей
user1.add_order("Суши", 1200)   # 1200 рублей
users.append(user1)

user2 = User("Мария", 28, "maria123")
user2.add_order("Бургер", 800)   # 800 рублей
users.append(user2)

# Функция для аутентификации
def authenticate_user(name, pin):
    for user in users:
        if user.name == name and user.pin == pin:
            return user
    return None

# Функция для входа в админку
def admin_login():
    name = input("Введите имя пользователя: ")

    # Проверка, содержит ли ник слово "admin"
    if "admin" not in name.lower():
        return  # Завершение функции, а значит и программы

    pin = input("Введите пароль: ")

    user = authenticate_user(name, pin)

    if user and user.is_admin:
        print("Добро пожаловать, администратор!")
        display_user_info()  # Отображаем информацию о пользователях
        display_orders()  # Отображаем заказы
    else:
        print("Неверное имя пользователя или пароль. Попробуйте еще раз.")
        # Можно добавить возможность повторного ввода
        retry = input("Хотите попробовать снова? (да/нет): ")
        if retry.lower() == 'да':
            admin_login()  # Рекурсивный вызов для повторного входа

# Функция для отображения информации о пользователях
def display_user_info():
    print("\n--- Информация о пользователях ---")
    for user in users:
        print(f"Имя: {user.name}, Возраст: {user.age}, Пароль: {user.pin}, Администратор: {user.is_admin}")

# Функция для отображения заказов
def display_orders():
    print("\n--- Заказы ---")
    for user in users:
        if user.orders:
            total_price_rub = 0
            total_price_usd = 0
            for order in user.orders:
                total_price_rub += order['цена']
                total_price_usd += order['цена_доллары']
                print(f"{user.name} заказал: {order['название']} за {order['цена']}р ({order['цена_доллары']:.2f}$)")
            print(f"Итого: {user.name} потратил {total_price_rub}р ({total_price_usd:.2f}$)")

# Запуск функции входа в админку
admin_login()