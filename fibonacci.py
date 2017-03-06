param1 = input("First number")
param2 = input("How many iterations")

def fibonacci(first, limit):
    import sys
    try:
        if any([first < 0, first == 0, limit < 0, limit == 0]):
            return -1
        else:
            x = first
            y = first + 1
            for i in range(limit):
                print(x)
                x, y = y, x+y
    except TypeError:
        sys.stdout.write("Make sure both your values are integers")

param1 = int(param1)
param2 = int(param2)        

fibonacci(param1, param2)
