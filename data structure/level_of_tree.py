class newNode:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


# Driver Code
if __name__ == '__main__' :

    # Let us construct the Tree shown
    # in the above figure
    root = newNode(3)
    root.left = newNode(2)
    root.right = newNode(5)
    root.left.left = newNode(1)
    root.left.right = newNode(4)

    num = int(input("enter number: "))
    print(f"{num}: {getLevel(root, num)}")
