def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    
    if target > high:
        return False

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        if arr[mid] < target:
            low = mid + 1
        if arr[mid] > target:
            high = mid - 1
    return False
