# Задані дані про потужність двигуна і вартість автомобілів
features = {
    'Tesla Model S': [1020, 1200000],
    'Ford Mustang': [450, 850000],
    'Chevrolet Camaro': [275, 900000],
    'BMW M3': [503, 1250000],
    'Audi RS7': [591, 1350000],
    'Mercedes-Benz S-Class': [429, 1450000],
    'Porsche 911': [83, 1800000],
    'Honda Civic': [99, 600000],
    'Toyota Corolla': [139, 400000],
    'Nissan GT-R': [565, 1700000]
}

# Функція для виведення на екран всіх значень словника
def print_features_car(features):
    for key, value in features.items():
        print(f"{key}: Потужність - {value[0]} к.с., Вартість - {value[1]} грн")


# Функція для додавання нового запису до словника
def add_new_car_and_features(features):
    new_key = input("Введіть назву автомобіля: ")
    force = int(input("Введіть потужність двигуна (к.с.): "))
    cost = int(input("Введіть вартість автомобіля (грн): "))
    features[new_key] = [force, cost]
    print(f"Додано новий автомобіль {new_key}")


# Функція для видалення запису зі словника
def delete_car(features):
    key_for_delete = input("Введіть назву автомобіля, який потрібно видалити: ")
    if key_for_delete in features:
        features.pop(key_for_delete)
        print(f"Видалено {key_for_delete}")
    else:
        print("Автомобіль не знайдено")


# Функція для перегляду вмісту словника за відсортованими ключами
def print_sorted_features(features):
    sorted_keys = sorted(features.keys())
    for key in sorted_keys:
        print(f"{key}: Потужність - {features[key][0]} к.с., Вартість - {features[key][1]} грн")


# Функція для обчислення загальної вартості автомобілів з потужністю понад 100 к.с.
def calculate_total_cost(features):
    total_cost = sum(value[1] for value in features.values() if value[0] > 100)
    print(f"Загальна вартість автомобілів з потужністю більше 100 к.с.: {total_cost} грн")


# Меню для вибору операції
def menu():
    while True:
        print("\nВиберіть операцію:")
        print("1. Показати всі автомобілі")
        print("2. Додати новий автомобіль")
        print("3. Видалити автомобіль")
        print("4. Показати автомобілі за відсортованими назвами")
        print("5. Порахувати загальну вартість автомобілів з потужністю > 100 к.с.")
        print("6. Вийти")

        choice = int(input("Ваш вибір: "))

        if choice == 1:
            print_features_car(features)
        elif choice == 2:
            add_new_car_and_features(features)
        elif choice == 3:
            delete_car(features)
        elif choice == 4:
            print_sorted_features(features)
        elif choice == 5:
            calculate_total_cost(features)
        elif choice == 6:
            print("Завершення програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


# Запуск програми
menu()
