def main():
    x = 1
    f = 4
    n = int(input("How long would you like your pi?: "))
    for j in range(0,n):
        z = f / x
        f = f * -1
        x = x + 2
