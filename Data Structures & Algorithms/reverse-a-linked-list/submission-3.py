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

        # so we did the reassignment at a higher level and return head 
        # the traversed aux arr is now pointed at null
        while (aux):
            aux.val = arr[i]
            aux = aux.next
            i += 1

        # at this point aux points now at null, but the og arr is now sorted
        # we can just return aux after reassining it to the now sorted og arr
        aux = head
        if aux:
            return aux
