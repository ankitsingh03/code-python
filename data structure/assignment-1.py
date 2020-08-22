class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


count = 0
def getfullCount(root):
    # Base Case
    if root is None:
        return 0

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize count
    queue.append(root)

    global count  # initialize count for full nodes
    while len(queue) > 0:
        node = queue.pop(0)

        # if it is full node then increment count
        if node.left is None and node.right is None:
            continue

        # Enqueue left child
        if node.left is None:
            node.left = Node(None)
            count += 1
        else:
            queue.append(node.left)

        # Enqueue right child
        if node.right is None:
            node.right = Node(None)
            count += 1
        else:
            queue.append(node.right)

    return count

# Function to print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)
    print()

lst =[]
def printGivenLevel(root, level):
    global lst
    if root is None:
        lst.append(None)
        return

    if level == 1:
        print(root.data, end=" ")
        lst.append(root.data)
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1



# Driver Program to test above function
tree = Node(5)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(7)
tree.left.left.left = Node(9)
tree.right.right = Node(1)
tree.right.right.left = Node(4)
tree.right.right.right = Node(6)


root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)


variable = root
getfullCount(variable)
print("Level order traversal of binary tree is -")
printLevelOrder(variable)
print(lst)
print(count)
