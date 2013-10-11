def fib(n):
    fib0 = 0
    fib1 = 1
    if n == 0:
        return fib0
    if n == 1:
        return fib1
    for i in range(n):
        temp = fib0 + fib1
        fib0 = fib1
        fib1 = temp
    return fib1

print fib(3)

print fib(5)
