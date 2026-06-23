class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        output.append(newInterval)
        return output


            

                
            
#   1----------4
#       1---------5

#          4-----------7
#                         8-------3

#  1---------4
#                5------7


#               4---------6

#  1--------------------6


#    1-----------3
#                      4--------------6
#        2----5