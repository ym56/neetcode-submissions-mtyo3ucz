# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            nextOne = cur.next # temp = 1
            cur.next = prev # 0.next = None
            prev = cur # None = 0
            cur = nextOne

        return prev