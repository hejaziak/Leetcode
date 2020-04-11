import math
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def height (node):
    if(node != None):
        return 1 + max(height(node.left), height(node.right))
    else:
        return 0
    
       
def depth(node):

    if(not node):
        return 0

    fromRoot = height(node.left) + height(node.right)
    leftNode = depth(node.left)
    rightNode = depth(node.right)

    return max(fromRoot, max(leftNode,rightNode)) 
    
class Solution(object):

        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return depth(root) 
        