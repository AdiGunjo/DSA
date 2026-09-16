import math


def jump_search(arr, target):
    n = len(arr)

    
    jump = int(math.sqrt(n))

    left = 0
    right = jump


    while left < n and arr[min(right, n) - 1] < target:
        left = right
        right += jump

        if left >= n:
            return -1

  
    while left < min(right, n):
        if arr[left] == target:
            return left

        if arr[left] > target:
            return -1

        left += 1

    return -1


arr = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))

target = int(input("Enter the number to search: "))

result = jump_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")