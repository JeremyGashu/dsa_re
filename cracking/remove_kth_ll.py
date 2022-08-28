# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        counter = 0
        while temp:
            counter += 1
            temp = temp.next
        tempHead = temp = head
        print(counter)
        if counter == n:
            return head.next

        c2 = 0
        while c2 < counter - n - 1:
            temp = temp.next
            c2 += 1

        if temp.next is not None:
            temp.next = temp.next.next

        return tempHead
