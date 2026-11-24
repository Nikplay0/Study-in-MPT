# № 1
def say_hi():
    print("Привет, мир !")

a = say_hi()
a
# № 2

def cube(x):
    return x

rectangle = cube
print(rectangle(2))
print(cube(3))

# № 3

def get_five():
    return 5

print(f"Тип функции: {type(get_five)} \nТип результата функции: {type(get_five())}\nТипы равны? {type(get_five) == type(get_five)}")

# № 4

def run_action():
    say_hi()

ra = run_action()
ra

# № 5

def step(a):
    return a*2


def aplly(action, number):
    res = number(action)
    print(res)

aplly(6, step)

# № 6

def tenp():
    a = []
    for i in range(1,4):
        a.append(i+10)
    return a 

def transform():
    print(tenp())

transform()

# № 7

def factory():
    def work():
        print("Работает")
    return work

factory()()


# № 8

def make_adder(value):
    def plus(x):
        return x + value

    return plus



print(make_adder(5)(7))
print(make_adder(7)(5))

def make_counter():
    k = 0
    def psi():
        nonlocal k
        k += 1
        return k 
    return psi

mc = make_counter()
print(mc())
print(mc())

