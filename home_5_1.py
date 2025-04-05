import keyword
import string

name = input("Введіть ім'я змінної: ")

    # Перевірка на наявність зареєстрованого слова
if name in keyword.kwlist:
    print(False)

    # Перевірка на те, чи починається з цифри
elif name[0].isdigit():
    print(False)

    # Перевірка на наявність великих літер
elif any(char.isupper() for char in name):
    print(False)

    # Перевірка на наявність пробілів
elif any(char == ' ' for char in name):
    print(False)

    # Перевірка на наявність заборонених символів
elif any(char in string.punctuation and char != "_" for char in name):
    print(False)

    # Перевірка на  підкреслення
elif len(name) >= 2 :
    if name[0] == '_' and name[1] == '_':
        print(False)
    else:
        print(True)
else:
    print(True)


