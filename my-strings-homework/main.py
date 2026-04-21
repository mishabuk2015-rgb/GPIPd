import poems
import sign

# Ім'я автора
author_name = "Михайло"

# Вивід шаблону з ім'ям
print(sign.SIGN_TEMPLATE.format(author_name))

# Побажання до курсу
wishes = "Бажаю цікавих практичних завдань!\nХочу більше прикладів з реального життя!"
print(wishes)

# Змінна з зірочками
stars = "**************************"

print(stars)
print(poems.POEM_ONE)
print(stars)
print(poems.POEM_TWO)
print(stars)
