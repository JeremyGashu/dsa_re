# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        pointer = None
        while temp:
            if pointer is None:
                pointer = ListNode(temp.val)
            else:
                t = ListNode(temp.val)
                t.next = pointer
                pointer = t
            temp = temp.next

        tempPointer = pointer
        tempHead = head
        while tempPointer is not None and tempHead is not None:
            if(tempPointer.val != tempHead.val):
                return False
            tempPointer = tempPointer.next
            tempHead = tempHead.next

        return True
