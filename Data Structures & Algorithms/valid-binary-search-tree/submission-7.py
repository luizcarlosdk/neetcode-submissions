# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#       5
#   1       8
#         6

# nodes_vals = [1, 6, 8]
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes_vals = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            nodes_vals.append(node.val)
            dfs(node.right)
        
        dfs(root)

        for i in range(1, len(nodes_vals)):
            if nodes_vals[i] <= nodes_vals[i-1]:
                return False
        
        return True