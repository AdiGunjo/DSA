import heapq


def funnel_sort(arr):
    """
    Funnel Sort implementation using a simplified
    k-way merge approach.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """

    n = len(arr)

    if n <= 1:
        return arr.copy()

    # Divide the array into smaller sorted runs
    runs = []
    chunk_size = max(1, int(n ** 0.5))

    for i in range(0, n, chunk_size):
        chunk = arr[i:i + chunk_size]
        chunk.sort()
        runs.append(chunk)

    # Merge all sorted runs using a min-heap
    heap = []

    for run_index, run in enumerate(runs):
        if run:
            heapq.heappush(
                heap,
                (run[0], run_index, 0)
            )

    result = []

    while heap:
        value, run_index, element_index = heapq.heappop(heap)
        result.append(value)

        next_index = element_index + 1

        if next_index < len(runs[run_index]):
            next_value = runs[run_index][next_index]

            heapq.heappush(
                heap,
                (next_value, run_index, next_index)
            )

    return result


# Example
numbers = [42, 7, 19, 3, 25, 1, 30, 15, 8]

print("Original:", numbers)

sorted_numbers = funnel_sort(numbers)

print("Sorted:", sorted_numbers)