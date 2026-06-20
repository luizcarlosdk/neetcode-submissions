# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1 cenario: root + root.left + root.right
# 2 cenario: root + root.left + root.left.left or the right
# 3 cenario: parent + root + root.left + root.right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = root.val

        def dfs(root):
            nonlocal max_val
            if not root:
                return 0
            
            left_max = dfs(root.left)
            right_max = dfs(root.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # update max_val with split:
            split_sum = root.val + left_max + right_max
            max_val = max(max_val, split_sum)

            # return to parent
            return root.val + max(left_max, right_max)
        
        dfs(root)
        return max_val