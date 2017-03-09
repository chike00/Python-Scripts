#Sn = n/2(2*a + d*(n-1)

a = int(input("Enter first number: "))
d = int(input("Enter the common difference: "))
n = int(input("Enter the range which this'll go up to: "))

def Sum(first, difference, Range):
    print((Range/2) * (2*first + difference*(Range-1)))

Sum(a, d, n)
