#генератор списка
def fib(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])
    print(f)

fib(20)

#функция с использованием yield
def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
fib1=fib(10)

for n in fib(10):
    print(n)
