# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashy = set()
        count = 0
        while (head):
            hashy.add(head)
            head = head.next
            if head in hashy:
                return True
        return False

        