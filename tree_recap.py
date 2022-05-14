class BinaryTreeNode:
    def __init__(self, data=0, right=None,left=None) -> None:
        self.right = right
        self.left = left
        self.data = data

    def addItem(self, item):
        if self.data:
            if item > self.data:
                if self.right:
                    self.right.addItem(item)
                else:
                    self.right = BinaryTreeNode(item)
            elif item < self.data:
                if self.left:
                    self.left.addItem(item)
                else:
                    self.left = BinaryTreeNode(item)

        else:
            self.data = item


    def printinOOrder(self):
        if self.data:
            if self.left:
                self.left.printinOOrder()
            print(self.data, end='  ')

            if self.right:
                self.right.printinOOrder()


head = BinaryTreeNode()
head.addItem(20)
head.addItem(12)
head.printinOOrder()
print()