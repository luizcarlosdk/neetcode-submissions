# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# questions about the input: 

# if the root is none return [[]] or []?

#   1 none 3, the return should include none?

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        levels = [[root.val]]

        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    level.append(curr.left.val)
                if curr.right:
                    q.append(curr.right)
                    level.append(curr.right.val)
            if level:
                levels.append(level)
        
        return levels
        