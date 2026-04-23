import messages as msg

# 1. Ім'я
name = input(msg.MSG_INPUT_NAME).strip()
if name.isalpha():
    print(msg.MSG_NAME_OK.format(name=name.title()))
else:
    print("Помилка: ім'я має містити лише літери!")

# 2. Вік
age = input(msg.MSG_INPUT_AGE).strip().lstrip("0")
if age.isdigit():
    print(msg.MSG_AGE_OK.format(age=age))
else:
    print("Помилка: вік має бути цілим числом!")

# 3. Телефон
phone = input(msg.MSG_INPUT_PHONE).strip()
if phone.isdigit():
    print(msg.MSG_PHONE_OK.format(phone=phone))
else:
    print("Помилка: телефон має містити лише цифри!")

# 4. Завершення
print(msg.MSG_FINISH)
