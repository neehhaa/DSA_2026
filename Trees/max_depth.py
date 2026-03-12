class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(9)
root.right.right = Node(10)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

def depth(root):
    if root is None:
        return 0
    left_height = depth(root.left)
    right_height = depth(root.right)

    return 1+max(left_height,right_height)

print(depth(root))
