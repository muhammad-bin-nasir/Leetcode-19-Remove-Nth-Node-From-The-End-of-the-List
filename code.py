# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        size = 0
        while temp is not None:
            temp = temp.next
            size = size+1
        if n == size:
            return head.next
        temp = head
        count = 0
        if size == 1:
            head = None
            return head
        for i in range(size-n-1):
            temp = temp.next
        temp.next = temp.next.next
        return head
        
