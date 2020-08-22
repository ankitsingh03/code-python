class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

tree = Node(5)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(7)
tree.left.left.left = Node(9)
tree.right.right = Node(1)
tree.right.right.left = Node(4)
tree.right.right.right = Node(6)

print("Level order traversal of binary tree is -")
printLevelOrder(tree)
print(lst)
