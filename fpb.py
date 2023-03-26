def fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))

print("FPB dari", num1, "dan", num2, "adalah", fpb(num1, num2))
