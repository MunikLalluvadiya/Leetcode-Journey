# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        crr = head
        l = 0
        while crr!=None:
            crr = crr.next
            l+=1
        
        crr = head
        for i in range(l//2):
            crr = crr.next
        return crr
        