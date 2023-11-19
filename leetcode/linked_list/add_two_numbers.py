# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, 
        l1: Optional[ListNode],
        l2: Optional[ListNode]) -> Optional[ListNode]:

        # l1_values = []
        # l2_values = []

        l1_value = 0
        l1_exponent = 0
        
        l2_value = 0
        l2_exponent = 0

        while l1 is not None:
            # l1_values.append(l1.val)
            l1_value += l1.val * pow(10, l1_exponent)
            l1_exponent += 1

            l1 = l1.next
        
        while l2 is not None:
            # l2_values.append(l2.val)
            l2_value += l2.val * pow(10, l2_exponent)
            l2_exponent += 1
            
            l2 = l2.next
        
        answer = l1_value + l2_value
        return answer

if __name__ == "__main__":
    sol = Solution()
    answer = sol.addTwoNumbers(l1=[2,4,3], l2=[5,6,4])
    print(answer)