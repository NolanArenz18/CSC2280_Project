n = eval(input("Please enter a whole positive number: "))
y = 1
z = 0
for v in range(0, n):
    if (v <= 1):
        x = v
    else:
        x = z + y
        z = y
        y = x
    print(x)
