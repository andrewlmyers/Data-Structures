class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right: 
            self.right.print()
    def search(self, value):
        # Base case: Non-existent node
        if self.data is None:
            return False

        # Base case: Found Match
        if value == self.data:
            return True

        # Recursive: Go to left or right subtree based on value
        if value <= self.data:
            if self.left is None:
                return False
            return self.left.search(value)
        else:
            if self.right is None:
                return False
            return self.right.search(value)

# FIND ODD NUMBERS
def tree_odds(node):
    if node is None:
        return 0
    left_odds  = tree_odds(node.left)
    right_odds = tree_odds(node.right)

    return node.data % 2 + left_odds + right_odds

arr = [1, 6, 20, 23, 19, 3, 5, 2]

tree = Node(8)
for i in arr:
    tree.insert(i)

tree.print() # 1 2 3 5 6 8 19 20

print(tree_odds(tree))
print(tree.search(4))
