# level

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

def level_order(root):
    from collections import deque
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.data, end= " ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

level_order(root)