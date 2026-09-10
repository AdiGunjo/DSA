import random


def quantum_sort(arr):

    while True:

        universe = arr.copy()

        random.shuffle(universe)

        if universe == sorted(universe):
            return universe


arr = [3, 1, 2]

print("Original:", arr)
print("Quantum Sort:", quantum_sort(arr))