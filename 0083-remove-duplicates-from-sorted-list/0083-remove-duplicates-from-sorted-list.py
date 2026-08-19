# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None :
            return head

        crr = head

        while crr != None and crr.next != None :
            if crr.next.val == crr.val:
                crr.next = crr.next.next
            else:
                crr = crr.next
        return head

        