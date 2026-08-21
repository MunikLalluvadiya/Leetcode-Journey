class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_half = prev

        # Step 3: compare first half and reversed second half
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