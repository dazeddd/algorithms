from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
            


if __name__ == "__main__":

    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(4)
    
    node2 = ListNode(1)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)

    sol = Solution()
    # print(node1.val)
    # print(node1.next.val)
    # print(node1.next.next.val)

    answer = sol.mergeTwoLists(node1, node2)
    # print(answer.val)
    # print(answer.next.val)
    # print(answer.next.next.val)
    # print(answer.next.next.next.val)
    # print(answer.next.next.next.next.val)

