list = [10, 45, 67, 88, 90]
x = 67

def binary_search(list, x):
    l = 0
    u = len (list)-1
    m = 0
    while l <=u:
        m = (l+u)//2
        if list[m] < x:
            l = m+1
        elif list[m] > x:
            u = m-1
        else:
            return m
    return -1
x= 45
result = binary_search(list,x)
if result !=-1:
    print("Found at position", result)

else:
    print("Result not found")
