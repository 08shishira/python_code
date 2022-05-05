# Recursion

def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
n = 3

if n <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fib(i))

# Using loops

# def fib(n):
#     a = 0
#     b = 1
#     if n <= 0:
#         print("Incorrect input")
#     elif n == 1:
#         print(a)
#     else:
#         for i in range(n):
#             print(a)
#             c= a+b
#             a,b = b,c
#             print(c)
#
# n = 3
# fib(n)
