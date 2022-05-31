from time import sleep
from turtle import left
from urllib.response import addinfo


class BinaryTreeNode:
    def __init__(self, data=0, right=None, left=None):
        self.right = right
        self.left = left
        self.data = data
    
    def addInOrder(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTreeNode(data)
                else:
                    self.left.addInOrder(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTreeNode(data)
                else:
                    self.right.addInOrder(data)

        else:
            self.data = BinaryTreeNode(data)

    def printInOrder(self):
        if self.left:
            self.left.printInOrder()
        print(self.data, end=', ')
        if self.right:
            self.right.printInOrder()

    def checkSymmetry(self):
        if not (self.right and self.left):
            return False
        
        # left, right = self.left, self.right
        # while left and right:
        #     if(left.left.data != )
        # return True







btn = BinaryTreeNode(10)
btn.addInOrder(20)
btn.addInOrder(34)
btn.addInOrder(4)
btn.addInOrder(2)


print(btn.checkSymmetry())