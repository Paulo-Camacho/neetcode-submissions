# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        aux = head

        arr = []
        while aux:
            arr.append(aux.val)
            aux = aux.next
        
        # re-arranging the O(n) arr
        left = 0
        right = len(arr) - 1
        reordered = []
        while left < right:
            reordered.append(arr[left])
            reordered.append(arr[right])
            left += 1
            right -= 1
        if len(arr) % 2 != 0:
            reordered.append(arr[left])
        print(reordered)

        i = 0
        while head:
            head.val = reordered[i]
            head = head.next
            i += 1
        
        
