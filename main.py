items = {}
while True:
    try:
        amount = int(input("Введіть кількість: "))
        item_type = input("Введіть тип: ")

        if item_type in items:
            items[item_type] += amount
            print(f"Оновлена кількість для {item_type}: {items[item_type]}")
        else:
            items[item_type] = amount
            print(f"Додано новий тип {item_type} з кількістю {amount}")
    except ValueError:
        print("Тут повинно бути число!!!")
    except Exception:
        print("Щось пішло не так...")