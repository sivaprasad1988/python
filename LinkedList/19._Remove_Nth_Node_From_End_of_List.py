class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = dummy

        for _ in range(n+1):
            left = left.next

        while left is not None:
            left = left.next
            right = right.next

        right.next = right.next.next

        return dummy.next





def print_list(head: ListNode):
    while head:
        print(head.val, end='  ')
        head = head.next
    print('None')


# Example usage
head = ListNode(1, None)

solution = Solution()

print_list(head)
head = solution.removeNthFromEnd(head, 1)

print("List after removing the nth node from end:")
print_list(head)
