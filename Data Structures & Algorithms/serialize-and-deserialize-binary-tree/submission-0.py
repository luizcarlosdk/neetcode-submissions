# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = []

        def dfs(node):
            if not node:
                output.append('N')
                return
            
            output.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(output)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if nodes[i] == 'N':
                i += 1
                return None
            
            new_node = TreeNode(nodes[i])
            i += 1
            new_node.left = dfs()
            new_node.right = dfs()
            return new_node

        return dfs()


