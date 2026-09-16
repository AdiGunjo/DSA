def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Example
arr = [3, 8, 10, 15, 25, 47]
result = binary_search_recursive(arr, 25, 0, len(arr) - 1)
print(f"Element found at index: {result}" if result != -1 else "Element not found")