#8.Определить, является ли год, который ввел пользователь, високосным или не високосным.


x = int(input('Введите год: '))
if ((x % 4 == 0) and not (x % 100 == 0)) or (x % 400 == 0):
    print("Високосный")
else:
    print("Обычный")