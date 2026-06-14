# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#  1 -> 2 -> 3

#  2 -> 3 -> 4

#

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            dummy_head = ListNode()
            current = dummy_head

            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    current = current.next
                    l1 = l1.next
                else:
                    current.next = l2
                    current = current.next
                    l2 = l2.next
            current.next = l1 or l2

            return dummy_head.next

        if len(lists) == 0:
            return None
        
        merged_list = lists[0]

        for i in range(1, len(lists)): #O(n) n being lists
            merged_list = mergeTwoLists(merged_list, lists[i]) #O(m) m = numbers of nodes
            
        return merged_list 

        # O (n * m)
        # O(1)