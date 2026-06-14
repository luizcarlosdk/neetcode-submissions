# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 -> 2 -> 3 -> 4 -> 5 -> len = 5 - 2 = 3 
#           c
#                len

# can n be higher than sz?

# d -> 1 -> 2 -> 3(x) -> 4
#           l
#                           r
# 2
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        l, r = dummy_node, head

        for _ in range(n):
            r = r.next
    
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return dummy_node.next


        
