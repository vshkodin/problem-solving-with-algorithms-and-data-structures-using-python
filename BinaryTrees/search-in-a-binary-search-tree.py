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

r = TreeNode(1)

r.insertLeft(11)
r.insertRight(12)

n1=r.getLeftChild()
n2=r.getRightChild()

n1_1=n1.insertLeft(21)
n1_2=n1.insertRight(22)

n2_1=n2.insertLeft(31)
n2_2=n2.insertRight(32)

# print("r.getRootVal() = ",r.getRootVal())
# print("r.getLeftChild() = ",r.getLeftChild())
#
# #right child
# r.insertLeft('b')
# c=r.getLeftChild()
# print(r.getLeftChild().getRootVal())
#
# c.insertLeft('D')
# print(c.getLeftChild().getRootVal())
# print(r.getLeftChild().getRootVal())

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

#https://stackoverflow.com/questions/41622174/inorder-binary-tree-traversal-using-python


class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        trav = root
        while trav:
            if trav.val == val:
                return trav
            elif trav.val < val:
                trav = trav.right
            else:
                trav = trav.left
s=Solution()
print(s.searchBST(r,12))
