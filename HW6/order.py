from letter import LETTER_TEMPLATE

# Запит даних у користувача
client_name = input("Введіть ім’я та прізвище: ")
trip_date = input("Введіть дату поїздки (наприклад, 10.06.2026): ")
persons = int(input("Введіть кількість осіб: "))

# Вартість за одну особу
price_per_person = 15000

# Загальна вартість
total_price = price_per_person * persons

# Логіка знижки
if persons > 5:
    discount = total_price * 0.05
else:
    discount = 0

# Фінальна ціна
final_price = total_price - discount

# Формування листа
letter = LETTER_TEMPLATE.format(
    name=client_name,
    date=trip_date,
    persons=persons,
    price_per_person=price_per_person,
    total_price=total_price,
    discount=int(discount),
    final_price=int(final_price)
)

# Вивід результату
print(letter)
