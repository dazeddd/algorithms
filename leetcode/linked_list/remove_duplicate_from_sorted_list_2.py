from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        pred = dummy

        # pred 와 별도로 체크하는
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                
                # skip all duplicates
                pred.next = head.next
            
            # Otherwise, move predecessor
            else:
                pred = pred.next

            head = head.next

        return dummy.next