def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # index found
    return -1  # not found

# Example
arr = [10, 25, 3, 47, 8, 15]
target = 47
result = linear_search(arr, target)
print(f"Element found at index: {result}" if result != -1 else "Element not found")