# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        i = 0
        idx_list = []
        current = head

        while current != None:
            idx_list.append(current)
            current = current.next
        
        j = len(idx_list) - 1

        while i < j:
            idx_list[i].next = idx_list[j]
            idx_list[j].next = idx_list[i+1]
            i += 1
            j -= 1
        
        idx_list[i].next = None