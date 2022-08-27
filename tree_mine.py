class BinaryTreeMine:
    def __init__(self, data=0, right=None, left=None) -> None:
        self.data = data
        self.right = right
        self.left = left

    def addInOrder(self, item):
        if self.data:
            if self.data > item:
                if self.left:
                    self.left.addInOrder(item)
                else:
                    self.left = BinaryTreeMine(item)

            else:
                if self.right:
                    self.right.addInOrder(item)
                else:
                    self.right = BinaryTreeMine(item)

        else:
            self.data = item

    def printInOrder(self):
        if self.data:
            if self.left:
                self.left.printInOrder()
            print(self.data, end='  ')
            if self.right:
                self.right.printInOrder()

        # print()


bt = BinaryTreeMine()
bt.addInOrder(10)
bt.addInOrder(300)
bt.addInOrder(5)
bt.addInOrder(2)
bt.printInOrder()
