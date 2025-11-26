# Definition for singly-linked list.
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr = ListNode(0)
        carry = 0

        while l1 or l2 or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            

if __name__ == "__main__":
    sol = Solution()
    answer = sol.addTwoNumbers(l1=[2,4,3], l2=[5,6,4])
    print(answer)