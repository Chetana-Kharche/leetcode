class Solution:
    def reorderList(self, head):

        if not head or not head.next:
            return
        
        # find mid
        slow=head
        fast=head

        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        # split ll
        second=slow.next
        slow.next=None

        # reverse secong half
        prev=None

        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt
        
        second=prev

        #merge
        first=head

        while second:
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second=temp2