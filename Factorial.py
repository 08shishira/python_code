#Recusrion

def fact(x):
    if x == 1:
        return 1
    else:
        return (x * fact(x-1))

x = 3
result = fact(x)
print(f"The Factorial of {x} is {result}")

#loop
# num = 9
#
# factorial = 1
#
# if num < 0:
#     print("Incorrect input")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, num+1):
#         factorial = factorial*i
#     print("The factorial of", num, "is", factorial)
