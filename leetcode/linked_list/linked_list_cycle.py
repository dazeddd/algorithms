from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        nodes_passed = set()

        while head is not None:

            if head in nodes_passed:
                return True
            nodes_passed.add(head)
            head = head.next # 다음 노드로 이동
        return False

