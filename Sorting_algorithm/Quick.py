def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range (low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick(arr, low, pi-1)
        quick(arr, pi+1, high)

data = [9,7,5,2,1,3,0]
quick(data, 0, len(data)-1)
print(data)
