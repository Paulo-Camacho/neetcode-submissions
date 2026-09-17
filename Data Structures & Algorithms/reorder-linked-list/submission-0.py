# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        aux = head
        while aux:
            nodes.append(aux.val)
            aux = aux.next
        left = 0
        right  = len(nodes) - 1
        rendered = []
        print(rendered)
        while left < right:
            rendered.append(nodes[left])
            rendered.append(nodes[right])
            left += 1
            right -= 1
        if len(nodes) % 2 != 0:
            rendered.append(nodes[left])
        i = 0
        while head:
            head.val = rendered[i]
            head = head.next
            i += 1
