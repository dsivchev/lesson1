# Functions - Задание 2
def format_price(price):
    price = int(price)
    formatted_price = "Цена: {} руб.". format(price)
    return formatted_price

p = format_price(56.24)
print(p)