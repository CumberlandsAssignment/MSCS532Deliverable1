class AVLNode:
    def __init__(self, key, product):
        self.key = key
        self.product = product
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, node, key, product):
        if not node:
            return AVLNode(key, product)

        if key < node.key:
            node.left = self.insert(node.left, key, product)
        else:
            node.right = self.insert(node.right, key, product)

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.balance(node)

        if balance > 1:
            return self.rotate_right(node)

        if balance < -1:
            return self.rotate_left(node)

        return node

    def range_query(self, node, low, high, result):
        if not node:
            return

        if low < node.key:
            self.range_query(node.left, low, high, result)

        if low <= node.key <= high:
            result.append(node.product)

        if high > node.key:
            self.range_query(node.right, low, high, result)