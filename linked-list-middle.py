# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Creating individual nodes
node1 = ListNode(1)
node2 = ListNode(2)
#node3 = ListNode(3)
#node4 = ListNode(4)
#node5 = ListNode(5)
#node6 = ListNode(6)

# Linking the nodes together to form the linked list
node1.next = node2
#node2.next = node3
#node3.next = node4
#node4.next = node5
#node5.next = node6

# The head of the linked list is node1
head = node1


# Function to print the linked list elements
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" , " if current.next else "")
        current = current.next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        count = 1
        while current and current.next:
            count += 1
            current = current.next

        middle = count // 2
        if middle == 0:
            return head

        i = 0
        while head:
            if i == middle:
                return head
            head = head.next
            i = i + 1


solution = Solution()
print_linked_list(solution.middleNode(head))
