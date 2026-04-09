# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursor = head
        prevNode = None
        while(cursor): # 0
            nNode = cursor.next # 1
            cursor.next = prevNode # 0 -> None
            prevNode = cursor # prevNode = 0
            if not nNode:
                break
            cursor = nNode # cursor = 1
        return cursor

