class Node:
    # A utility function to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


count = 0
lst = []


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

        # this will check leaf node
        if node.left is None and node.right is None:
            continue

        if node.left is None:
            node.left = Node(None)
            count += 1
        else:
            queue.append(node.left)

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


def printGivenLevel(root, level):
    global lst
    if root is None:
        lst.append(None)
        return

    if level == 1:
        # print(root.data, end=" ")
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


# give level of element in tree
def getLevelUtil(node, data, level):
    if node == None:
        return 0

    if node.data == data:
        return level

    downlevel = getLevelUtil(node.left, data, level + 1)

    if downlevel != 0:
        return downlevel

    downlevel = getLevelUtil(node.right, data, level + 1)
    return downlevel


# Returns level of given data value
def getLevel(node, data):
    return getLevelUtil(node, data, 1)


# this function give distance between two element
def distance(node, val1, val2):
    if getLevel(node, val1) == getLevel(node, val2):
        return abs(lst.index(val2) - lst.index(val1)) - 1
    else:
        return "level will not get match"


# Driver Program to test above function
node = Node(5)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(7)
node.left.left.left = Node(9)
node.right.right = Node(1)
node.right.right.left = Node(4)
node.right.right.right = Node(6)


# make this variable to save time.
variable = node

getfullCount(variable)
printLevelOrder(variable)

# it will give distance and count
print(f"horizontal distance between 2 nodes at the same level: {distance(variable, 7, 1)}")
print(f"counting the position where the node is not present: {count}")
