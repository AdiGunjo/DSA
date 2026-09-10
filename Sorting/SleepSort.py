import threading
import time

def sleep_sort(arr):
    result = []
    threads = []

    def wake_up(num):
        time.sleep(num * 0.01)
        result.append(num)

    for num in arr:
        thread = threading.Thread(target=wake_up, args=(num,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result


arr = [5, 2, 8, 1, 3]

print("Original:", arr)
print("Sleep Sort:", sleep_sort(arr))