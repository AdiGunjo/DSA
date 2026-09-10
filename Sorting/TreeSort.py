class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):

    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def inorder(root, result):

    if root is not None:
        inorder(root.left, result)
        result.append(root.value)
        inorder(root.right, result)


def tree_sort(arr):

    root = None

    for num in arr:
        root = insert(root, num)

    result = []

    inorder(root, result)

    return result


arr = [5, 2, 8, 1, 3]

print("Original:", arr)
print("Tree Sort:", tree_sort(arr))