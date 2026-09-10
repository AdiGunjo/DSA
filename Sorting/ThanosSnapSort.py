import random


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


def thanos_sort(arr):

    result = arr.copy()

    while not is_sorted(result):

        if len(result) <= 1:
            return result

        # Thanos eliminates half
        result = random.sample(
            result,
            len(result) // 2
        )

    return result


arr = [5, 2, 8, 1, 3, 7]

print("Original Array:", arr)
print("Thanos Sorted:", thanos_sort(arr))