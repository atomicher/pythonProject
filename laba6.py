def split_list(input_list, split_index):
    if split_index < 0 or split_index > len(input_list):
        print("Невірний індекс для розбиття!")
        return

    # Розбиття списку на дві частини
    list1 = input_list[:split_index]
    list2 = input_list[split_index:]

    print("Перша частина списку:", list1)
    print("Друга частина списку:", list2)

try:
    user_input = input("Введіть елементи списку через пробіл: ").split()
    split_index = int(input("Введіть порядковий номер елемента для розбиття (індекс): "))

    # Виклик функції для розбиття списку
    split_list(user_input, split_index)

except ValueError:
    print("Помилка: введіть правильні числові дані.")
