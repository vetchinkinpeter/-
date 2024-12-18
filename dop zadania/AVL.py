class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y


    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)


        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)


        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)


        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)


        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)


        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)
a = AVLTree()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
for num in nums:
    a.insert(num)


