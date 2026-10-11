#СТРОКИ 

# № 1
#a = '123456'
# print(len(a), a[0], a[-1])

# № 2
a = '1234567'
center = len(a)//2
if len(a) % 2 == 0:
    print(a[center - 1: center + 1])
else:
    print(a[center])


# № 3

# print(a[0:3]) #получаем первый три символа строки
# print(a[-3:]) #получаем последние три символа строки
# print(a[::2]) # все символы с чётными индексами.
# print(a[::-1]) #строка в обратном порядке.

# № 4
# b = "Яблоко АНАНАС банан"

# print(b.capitalize())
# print(b.lower())
# print(b.upper())

# № 5

# c = "ананас"
# print("с" in c)
# print(c.count("с"))
# print(c.find("с"))

# № 6
# b = "Яблоко АНАНАС банан"
# print(b.replace(" ", "_"))

# № 7

# b = " Яблоко "
# print("Начальная длина строки", len(b))
# delete = b.replace(" ", "")
# print("Конечная длина строки", len(delete))

# № 8

# name = "Николай Лебедев"
# ot = name.split()
# print(f"Фамилия: {ot[1]}\n Имя: {ot[0]} \n Инициалы: {ot[1][0]}. {ot[0][0]}.")

# № 9

# word = "Радар"
# low = word.lower()
# if low == low[::-1]:
#     print(f"{word} - это палиндром")
# else:
#     print(f"{word} - это не палиндром")

# № 10

# b = "Яблоко АНАНАС банан"
# fruits = b.split()

# print(f" Количество слов: {len(fruits)}. Первое слово {fruits[0]}. Последнее слово {fruits[-1]}")




