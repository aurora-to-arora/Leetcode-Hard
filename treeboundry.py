'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        # code here
        if not root:
            return
        res=[root.data]
        
        def isLeaf(node):
            return not node.left and not node.right
        
        def leftboundry(node):
            while node:
                if not isLeaf(node):
                    res.append(node.data)
                node= node.left if node.left else node.right
                
        
        def addLeaves(node):
            if not node:
                return
            if isLeaf(node):
                res.append(node.data)
                return
            addLeaves(node.left)
            addLeaves(node.right)
        
        def rightboundry(node):
            temp=[]
            while node:
                if not isLeaf(node):
                    temp.append(node.data)
                node = node.right if node.right else node.left
            res.extend(temp[::-1])
        
        if root.left:
            leftboundry(root.left)
        
        addLeaves(root.left)
        addLeaves(root.right)
        
        if root.right:
            rightboundry(root.right)
            
        return res
                    
        
        
