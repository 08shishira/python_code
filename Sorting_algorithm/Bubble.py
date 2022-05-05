def bubble(arr):
    k = len(arr)
    for i in range (k):
        for j in range(k-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [9,7,1,2,5,0,4]
m = bubble(arr)
print(m)
