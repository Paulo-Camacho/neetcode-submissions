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
        # we are resetting this such that we can reassign
        aux = head
        i = 0
        while (aux):
            aux.val = arr[i]
            aux = aux.next
            i += 1
        aux = head
        # so we did the reassignment at a higher level and return head 
        # the traversed aux arr is now pointed at null
        if aux:
            return aux
