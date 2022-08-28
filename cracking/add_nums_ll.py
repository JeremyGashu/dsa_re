# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = res = ListNode()
        carry = 0
        templ1, templ2 = l1, l2
        while templ1 or templ2 or carry != 0:
            val = carry
            if templ1 is not None:
                val += templ1.val
            if templ2 is not None:
                val += templ2.val

            if val >= 10:
                res.next = ListNode(val - 10)
                res = res.next
                carry = 1
            else:
                res.next = ListNode(val)
                res = res.next
                carry = 0

            if templ1 is not None:
                templ1 = templ1.next
            if templ2 is not None:
                templ2 = templ2.next
        return temp.next
