# №1 

# def say_hello():
#     print("Привет, мир!")

# say_hello()
# say_hello()

# №2

# def greet(name):
#     print(f"Привет, {name}!")

# greet("Анна")
# greet("Олег")

#  №3

# def add(a,b):
#     return a + b

# print(add(3,5))

# №4

# def greet(name = "Гость"):
#     print(f"Привет, {name}!")

# greet("Анна")
# greet()

#  №5

# def substract(a,b):
#     return a - b

# print(substract(5,1))
# print(substract(a = 5, b = 2))

# №6

# def introduce(name, city = "Москва"):
#     print(f"Меня зовут {name}, я из {city}")

# introduce("Олег Коффи", "")
# introduce("Олег Коффи", "Маями")

# №7

def multiply(*number):
    res = 1
    for i in number:
        res *= i
    return res
print(multiply(1,2,3,4))

# №8

def display_info(**args):
    for key, value in args.items():
        print(f"{key}: {value}")

display_info(name="Анна", age=28, city="Москва") 

# # №9
def order(name_o, *dop_position, kol = 1):
    print(f"Корзина \n Название товара: {name_o}. \n Количество: {kol}. \n Дополнение: {dop_position}.")

order("Яблоко", 2, "Макароны", "Картошка", "Хлеб")

# №10

def profile(name, age, **args):
    result = [f"Имя: {name}", f"Возраст: {age}"]
    for key, value in args.items():
        result.append(f"{key}:{value}")
    return result
print(profile("Иван", 12, город ="Москва", хобби ="Волейбол"))
