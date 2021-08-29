class Solution:
    
    def helper(self, head, n):
        """reverses the first n elements of the list"""
        new_list = None
        orig_head = head
        for _ in range(n):
            temp = head
            head = head.next
            temp.next = new_list
            new_list = temp
        orig_head.next = head
        return new_list
            
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = dummy
        for _ in range(left - 1):
            curr = curr.next
        curr.next = self.helper(curr.next, right - left + 1)
        return dummy.next