# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # combine list and return it as the new linked list
        aux1 = list1
        aux2 = list2
        new_list1 = []
        new_list2 = []
        while (aux1):
            new_list1.append(aux1.val)
            aux1 = aux1.next
        while (aux2):
            new_list2.append(aux2.val)
            aux2 = aux2.next
        arr  = new_list1 + new_list2
        arr.sort()
        new_head = list1
        # converting the arr into a linked list (how would I get the entire span of new sum arrs)

        if len(new_list1) == 0 and len(new_list2) == 0:
            return
        head = ListNode()
        if arr :
            head = ListNode(arr[0])
        curr = head
        for val in range(1, len(arr)):
            curr.next = ListNode(arr[val])
            curr = curr.next
            print(curr.val)
        return head


