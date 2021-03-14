class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = TreeNode(newNode)
        else:
            t = TreeNode(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self,newNode):
        if self.right == None:
            self.right = TreeNode(newNode)
        else:
            t = TreeNode(newNode)
            t.right = self.right
            self.right = t


    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setRootVal(self,obj):
        self.val = obj

    def getRootVal(self):
        return self.val

r = TreeNode('a')
print("r.getRootVal() = ",r.getRootVal())
print("r.getLeftChild() = ",r.getLeftChild())

#right child
r.insertLeft('b')
c=r.getLeftChild()
print(r.getLeftChild().getRootVal())

c.insertLeft('D')
print(c.getLeftChild().getRootVal())
print(r.getLeftChild().getRootVal())

# #Left child
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# #overwrite Left child
# r.insertLeft('d')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
# #overwrite righ child to hello
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())
# # add child to right heloo child Tolian

