# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        temp = None
        while cur:
            nextOne = cur.next # temp = 1
            cur.next = temp # 0.next = None
            temp = cur # None = 0
            cur = nextOne

        return temp