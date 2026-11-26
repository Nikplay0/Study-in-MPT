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


def run_action(action):
    action()

run_action(say_hi)

# № 5

def step(a):
    return a*2


def aplly(action, number):
    res = action(number)
    print(res)

aplly(step, 6)

# № 6

def transform(values, action):
    a = []
    [action(x) for x in values]
    for i in values:
        nvalue = action(i)
        a.append(nvalue)
    return a

def tenp(n):
    return n + 10

result = transform([1,2,3], tenp)

print(result)


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

