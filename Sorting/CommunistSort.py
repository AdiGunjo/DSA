def communist_sort(arr):
    if not arr:
        return []

    average = sum(arr) / len(arr)

    return [average] * len(arr)


arr = [5, 2, 8, 1, 3]

print("Original Array:", arr)
print("Communist Sorted:", communist_sort(arr))