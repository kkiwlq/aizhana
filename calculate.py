print("=== КАЛЬКУЛЯТОР ===")

while True:
    print("\nВыберите действие:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("0. Выход")

    choice = input("Ваш выбор: ")

    if choice == "0":
        print("Калькулятор выключен!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Ошибка! Выберите правильную операцию.")
        continue

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if choice == "1":
        print("Результат:", num1 + num2)

    elif choice == "2":
        print("Результат:", num1 - num2)

    elif choice == "3":
        print("Результат:", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("Ошибка! На ноль делить нельзя.")
        else:
            print("Результат:", num1 / num2)