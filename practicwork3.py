#Список
# № 1

# list = [1,2,3,4]
# print(f"Первый элемент: {list[0]}\n Последний элемент {list[-1]}")
# rt = list[::-1]
# print(rt)

# № 2

# list = [1,2,3,4,5]
# center = len(list)//2

# if len(list) % 2 == 0:
#     print(list[center - 1 : center + 1])
# else:
#     print(f"Элемент середины списка {list[center]}")

# № 3

# list = [1,2,3,4,5,6,7,8,9,10]
# print(list[0:3])
# print(list[-3:])
# print(list[::2])
# print(list[::-1])

# № 4

# list = []
# Первый вариант

# my_list = [1] + list + [4,5,6]
# del my_list[-1]

# Второй вариант
# list.extend([4,5,6])
# list.insert(0,1)
# del list[-1]
# print(list)

#  № 5

# list = [1,2,3,4,5]
# print(list)
# print(f"Длина: {len(list)}, Сумма: {sum(list)}, Минимум: {min(list)}, Максимум: {max(list)}, Среднее арифметическое: {sum(list)/len(list)}")

# № 6

# list = [1,2,3,4,4,5,2] 

# print(5 in list)
# print(list.count(5))
# print(list.index(5))

#  № 7

# list = [9,8,6,7,4,5,2,3,1]
# sorted = sorted(list)
# print(f"Три наименьших: {sorted[:3]}. Три наибольших: {sorted[-3:]}")

# № 8

# list1 = [2,1,5,4]
# list2 = [3,6,8,7]
# Первый способ
# list = list1 + list2
# sort_list = sorted(list, reverse = True)
# print(sort_list[1])

# # Второй способ
# list1.extend(list2)
# sort = sorted(list1)
# sort_list = sort[::-1]
# print(sort_list[1])

#  № 9 

# b = "Яблоко АНАНАС банан"
# c = b.lower()
# list = c.split()
# sort_list = sorted(list)
# stroka = ",".join(sort_list)
# print(stroka)

# № 10
list = [1,2,3,4,5]
k = 2
n = len(list)
k = k%n
list = list[k:] + list[:k]
print(list)





