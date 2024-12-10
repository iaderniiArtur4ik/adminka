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
        while True:
            action = input(
                "Выберите действие: 1 - Просмотр пользователей, 2 - Просмотр заказов, 3 - Добавить заказ, 4 - Выйти: ")
            if action == '1':
                display_user_info(user)  # Отображаем информацию о пользователях, исключая администратора
            elif action == '2':
                display_orders()  # Отображаем заказы
            elif action == '3':
                add_order_for_user()  # Добавляем заказ для пользователя
            elif action == '4':
                print("Вы вышли из админки.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
    else:
        print("Неверное имя пользователя или пароль. Попробуйте еще раз.")
        # Можно добавить возможность повторного ввода
        retry = input("Хотите попробовать снова? (да/нет): ")
        if retry.lower() == 'да':
            admin_login()  # Рекурсивный вызов для повторного входа


# Функция для отображения информации о пользователях
def display_user_info(admin_user):
    print("\n--- Информация о пользователях ---")
    for user in users:
        if user != admin_user:  # Пропускаем администратора
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


# Функция для добавления заказа для пользователя
def add_order_for_user():
    user_name = input("Введите имя пользователя, для которого хотите добавить заказ: ")
    user = next((u for u in users if u.name == user_name), None)

    if user:
        order_name = input("Введите название заказа: ")
        price_rub = float(input("Введите цену заказа в рублях: "))
        user.add_order(order_name, price_rub)
        print(f"Заказ '{order_name}' на сумму {price_rub}р успешно добавлен для пользователя {user.name}.")
    else:
        print("Пользователь не найден.")


# Запуск функции входа в админку
admin_login()