# # Множества
# # № 1
# list = [1,1,2,2,3,3,4,4,4]
# a = set(list)
# print(f"Множество {a}. Длина множества {len(a)}")

# № 2
# a = {1,2,3}
# a.add(4)
# a.remove(1)
# print(a)

# № 3
# a = {1,2,3}
# b = {4,5,6}
# c = a.union(b)
# print(c)

# № 4
# a = {1,2,3,4,7}
# b = {2,3,4,5,6}
# print(a.intersection(b), a & b)

# № 5
# a = {1,2,3,4,7}
# b = {2,3,4,5,6}
# print(f"Элементы первого: {a.difference(b)} Элементы второго: {b.difference(a)}")

# № 6
# a = {1,2,3,4,7}
# b = {2,3,4,5,6}
# print(a^b)

# № 7
# a = {1,2,3,4,7}
# x = int(input("Введите число: "))
# if x in a:
#     print(f"{x} есть в множестве")
# else:
#     print(f"{x} нет в множестве")

#  № 8

# toys = {"Машинки", "Поезда", "Мяч", "Солдатики"}
# cars = {"Машинки"}
# print(cars.issubset(toys))

#  № 9
# a = "924531678"
# print(f"{set(a)}. Длина строки: {len(set(a))}")

# № 10
a = [7,8,3,1,2]
b = [10,4,5,6,3]
print(sorted(set(a + b)))
