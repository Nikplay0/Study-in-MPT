print("  ==КАЛЬКУЛЯТОР==")
a = float(input("Введите первое число "))
b = float(input("Введите второе число "))
dei = int(input("Каталог действий:\n 1 - Сравнение\n 2 - арифметические вычисления\n 3 - операторы принадлежности\n 4 - операторы тождественности \n 5 - логические операторы \n Введите номер нужного вам действия: "))
if dei == 1:
    sravnenie = int(input("Каталог сравнения: \n 1 - равно/не равно(помогает узнать равняются ли числа) \n 2 - Больше/Меньше(помогает узнать меньши или больше, одно число другого)\n 3 - Больше или равно/Меньше или равно(позволяет узнать меньше или равно/больше или равно одно число другого)\n Введите номер нужного вам сравнения: "))
    if sravnenie == 1:
        if a == b:
            print("Числа ранвы")
        else: 
            print("Числа не равны")
    if sravnenie == 2:
        if a > b:
            print(f"{a} больше  {b}")
        else:
            print(f"{a} меньше {b}")
    if sravnenie == 3:
        if a>=b:
            print(f"{a} больше или равно {b}")
        else:
            print(f"{a} меньше или равно {b}")   
elif dei == 2:
    arifmeti = int(input("Каталог вычислений: \n 1 - Сложение \n 2 - Вычитание \n 3 - Умножение \n 4 - Деление \n 5 - Целочисленное деление \n 6 - Остаток от деления \n 7 - Возведение в степень \n Введите номер нужного вам действия: "))
    if arifmeti == 1:
        print(a+b)
    elif arifmeti == 2:
        print(a - b)
    elif arifmeti == 3:
        print(a*b)
    elif arifmeti == 4:
        if b == 0:
            print("На ноль делить нельзя")
        else:
            print(a/b)
    elif arifmeti == 5:
        if b == 0:
            print("На ноль делить нельзя")
        else:
            print(a//b)
    elif arifmeti == 6:
        if b == 0:
            print("На ноль делить нельзя")
        else:
            print(a%b)
    elif arifmeti == 7:
        print(a**b)
elif dei == 3:
    pri = int(input("Каталог операторов принадлежности: \n 1 - in() \n 2 - not in() \n Введите номер нужного вам оператора принадлежности: "))
    if pri == 1:
        a = ''
        b = ''
        print(a in b)
    if pri == 2:
        a = ''
        b = ''
        print(a not in b) 
elif dei == 4:
    tosh = int(input("Каталог операторов тождественности: \n 1 - is \n 2 - in not \n Введите номер нужного вам оператора тождественности: "))
    if tosh == 1:
        print(a is b)
    if tosh == 2:
        print(a is not b)                    
elif dei == 5:
    loghich = int(input("Каталог логических операторов: \n 1 - or(логическое или) \n 2 - and(логическое и) \n 3 - not(логическое отрицание) \n Введите номер нужного вам логического оператора: " )) 
    if loghich == 1:
        print(a>0 or b>0)
    if loghich == 2:
        print(a < 0 and b < 0)
    if loghich == 3:
        print(not(b>0))
else:
    print("Ошибка")