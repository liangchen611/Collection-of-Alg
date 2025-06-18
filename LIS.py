def lower_bound(arr, target):
    low, high = 0, len(arr)
    while low<high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid+1
        else:
            high = mid
    return low

s = [2,3,4,5,6,7]
l = lower_bound(s,3)
print(l)