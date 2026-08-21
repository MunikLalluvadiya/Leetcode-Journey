class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
  
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_half = prev

       
        first_half = head
        result = True
        p1, p2 = first_half, second_half
        while p2:
            if p1.val != p2.val:
                result = False
                break
            p1 = p1.next
            p2 = p2.next

        return result