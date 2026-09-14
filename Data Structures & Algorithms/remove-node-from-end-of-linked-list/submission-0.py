# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        track = 0
        # make an arr then convert back to linked list
        bruh = []
        arr = []
        aux = head 

        while (aux):
            bruh.append(aux.val)
            aux = aux.next
        print(bruh)

        aux = head 

        z = len(bruh)
        while (aux):
            if n != z:
                print(f'z: {z} n: {n}', end=" ")
                print(f'added: {aux.val}')
                arr.append(aux.val)
            aux = aux.next
            z -= 1
        print(arr)

        start = None
        if arr:
            start = ListNode(arr[0])
        curr = start
        for i in range(1, len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next
        return start


