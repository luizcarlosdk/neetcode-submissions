# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# can i assume i have the definition of a node, or need to create it?
# if they're empty, just return and empty None?
# bst or just bt?
#        1
#     2      3
#               4
# inorder = 2, 1, 3, 4
#              m
# preorder = 1, 2, 3, 4


# left tree

#  preorder[1, mid + 1]
#  inorde[0:mid]

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0]) 
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid+1:len(preorder)], inorder[mid+1:len(inorder)])

        return root

                