import random


def is_sorted(arr):
    return all(
        arr[i] <= arr[i + 1]
        for i in range(len(arr) - 1)
    )


def apocalypse_sort(arr):

    result = arr.copy()

    while len(result) > 1:

        if is_sorted(result):
            return result

        # Random apocalypse
        index = random.randrange(len(result))

        del result[index]

    return result


arr = [5, 2, 8, 1, 3, 7]

print("Original:", arr)
print("Apocalypse Sort:", apocalypse_sort(arr))