# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #split list
        current = slow.next
        slow.next = prev = None
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        #merge
        firsthalf, secondhalf = head, prev
        while secondhalf:
            tmp1, tmp2 = firsthalf.next, secondhalf.next
            firsthalf.next = secondhalf
            secondhalf.next = tmp1
            firsthalf, secondhalf = tmp1, tmp2
        

        