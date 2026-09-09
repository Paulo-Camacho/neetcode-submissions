# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        decouple = head
        while (decouple):
            arr.append(decouple.val)
            decouple = decouple.next
        print(arr)
        arr.reverse()
        print(arr)
        i = 0
        decouple = head
        while (decouple):
            decouple.val = arr[i]
            decouple = decouple.next
            i += 1
        if head:
            return head