def fibonacci(first, limit):
    x = first
    y = first + 1
    for i in range(limit):
        print(x)
        x, y = y, x+y


fibonacci(1, 10)
