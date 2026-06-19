# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#       2    
#    1     3

# 1    0



class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = 0
        ans = root.val 
        def dfs(node, k):
            nonlocal curr, ans
            if not node:
                return
            
            dfs(node.left, k)
            curr += 1
            if curr == k:
                ans = node.val
                return
            dfs(node.right, k)
        dfs(root, k)
        return ans