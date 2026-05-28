# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current_pointer = head
        previous = None
        reversed_ref = None

        while current_pointer:

            reversed_ref = current_pointer
            current_pointer = current_pointer.next
            reversed_ref.next = previous
            previous = reversed_ref
        
        return previous
            


        