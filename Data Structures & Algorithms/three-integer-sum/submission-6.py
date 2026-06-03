class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()

#  -4 -2 -2 2 2
#   i    l
#           r

        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1

            while l < r:
                curr_sum = nums[l] + nums[r]

                # -4 -1 0 2 2
                # cu

                if curr_sum == -nums[i]:
                    output.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif curr_sum < -1*(nums[i]):
                    l += 1
                else:
                    r -= 1
        
        return [list(i) for i in output]        

        