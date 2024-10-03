# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(value):
    if not value:
        return None

    head = ListNode(value[0])
    current = head
    for val in value[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end="")
        current = current.next


# Creating two linked lists
list1_values = [2, 4, 0]
list2_values = [5, 6, 11]

linked_list1 = create_linked_list(list1_values)
linked_list2 = create_linked_list(list2_values)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        current = head
        carry = 0
        if l1 is not None or l2 is not None:
            while l1 is not None or l2 is not None or carry != 0:

                x = l1.val if l1 is not None else 0
                y = l2.val if l2 is not None else 0

                total = x + y + carry
                result = total % 10
                carry = total // 10
                current.next = ListNode(result)
                current = current.next

                if l1 is not None:
                    l1 = l1.next
                if l2 is not None:
                    l2 = l2.next

            return head.next


s = Solution()

print_linked_list(s.addTwoNumbers(linked_list1, linked_list2))
