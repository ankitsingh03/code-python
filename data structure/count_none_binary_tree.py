class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def getfullCount(root):
    # Base Case
    if root is None:
        return 0

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize count
    queue.append(root)

    count = 0  # initialize count for full nodes
    while len(queue) > 0:
        node = queue.pop(0)

        # if it is full node then increment count
        if node.left is None and node.right is None:
            continue

        # Enqueue left child
        if node.left is None:
            count += 1
        else:
            queue.append(node.left)

        # Enqueue right child
        if node.right is None:
            count += 1
        else:
            queue.append(node.right)

    return count




# Driver Program to test above function
root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)

tree = Node(5)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(7)
tree.left.left.left = Node(9)
tree.right.right = Node(1)
tree.right.right.left = Node(4)
tree.right.right.right = Node(6)

print(getfullCount(tree))
