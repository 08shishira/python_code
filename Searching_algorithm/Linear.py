pos = 0
def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            global pos
            pos = i
            return True
    return False

list = [1,2,7,8,3,9]
n = 4
if search(list, n):
    print("Found at postion", pos+1)
else:
    print("Not found")
