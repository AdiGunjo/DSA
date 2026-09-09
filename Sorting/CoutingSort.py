def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    counts = [0] * (max_val + 1)

    for num in arr:
        counts[num] += 1

    result = []
    for num, count in enumerate(counts):
        result.extend([num] * count)
    return result

print(counting_sort([4, 2, 2, 8, 3, 3, 1]))