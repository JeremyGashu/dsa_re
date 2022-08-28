
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        seen = {}
        while temp:
            seen[temp.val] = seen.get(temp.val, 0) + 1
            temp = temp.next

        temp = head
        headTemp = tempTemp = ListNode()
        while temp:
            if(seen[temp.val] <= 1):
                tempTemp.next = ListNode(temp.val)
                tempTemp = tempTemp.next
            temp = temp.next

        return headTemp.next
