class Solution:
    def reverseKGroup(self, head, k):

        # Step 1: Check if k nodes are available
        curr = head
        count = 0

        while curr and count < k:
            curr = curr.next
            count += 1

        # Less than k nodes → don't reverse
        if count < k:
            return head

        # Step 2: Reverse k nodes
        prev = None
        curr = head

        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Connect remaining list
        head.next = self.reverseKGroup(curr, k)

        # prev is the new head
        return prev