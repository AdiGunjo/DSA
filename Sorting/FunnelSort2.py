def funnel_sort(arr):
    import math

    def merge(lo, mid, hi):
        i, j = lo, mid + 1

        while i <= mid and j <= hi:
            if arr[i] <= arr[j]:
                i += 1
            else:
                val = arr[j]

                for k in range(j, i, -1):
                    arr[k] = arr[k - 1]

                arr[i] = val
                i += 1
                mid += 1
                j += 1

    def funnel_merge(lo, hi):
        size = hi - lo + 1

        if size <= 1:
            return

        if size <= 4:
            for i in range(lo + 1, hi + 1):
                j = i

                while j > lo and arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
                    j -= 1

            return

        k = max(2, math.ceil(math.sqrt(size)))
        seg_size = math.ceil(size / k)

        for s in range(k):
            seg_lo = lo + s * seg_size
            seg_hi = min(lo + (s + 1) * seg_size - 1, hi)

            if seg_lo <= seg_hi:
                funnel_merge(seg_lo, seg_hi)

        run = seg_size

        while run < size:
            s = lo

            while s <= hi:
                mid = min(s + run - 1, hi)
                end = min(s + run * 2 - 1, hi)

                if mid < end:
                    merge(s, mid, end)

                s += run * 2

            run *= 2

    funnel_merge(0, len(arr) - 1)
    return arr

numbers = [42, 7, 19, 3, 25, 1, 30, 15, 8]

print("Before:", numbers)

funnel_sort(numbers)

print("After:", numbers)