# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 make node array : using aux head
        # reverse said array
        # using the aux arr for the return
        aux = head
        arr = []
        while (aux):
            print(aux.val)
            arr.append(aux.val)
            aux = aux.next
        # reseting the aux node 
        arr.reverse()
        aux = head
        i = 0
        while (aux):
            aux.val = arr[i]
            aux = aux.next
            i += 1
        if head:
            return head 
