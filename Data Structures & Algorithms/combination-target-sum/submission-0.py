# distrinct nums
# target: int

# combinmations -> sums sum to target
# 3 3 3 4 = 4 3 3 3

# return [] if None
# negative numbers?

# retun list[list[int]]?

# 2 5 6 9
#   i

# Base total > target, i > len(list)
#


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        
        def dfs(i, curr, total):
            if total == target:
                output.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            #left
            dfs(i, curr, total + nums[i])
            #right
            curr.pop()
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return output
        