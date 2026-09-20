print("x y")
for x in 0,1:
    for y in 0, 1:
        F = (x or y) and (not(x) or not(y))
        print(x, y, F)
print("Hello world!!!")

