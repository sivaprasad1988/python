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
        print(current.val, end="->")
        current = current.next


# Creating two linked lists
list2_values = [5, 6, 11, 9]

linked_list = create_linked_list(list2_values)

print_linked_list(linked_list)
class Solutions:

    def reverseList(self, head):
        previous = None
        current = head

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        return previous

ll = Solutions()

print_linked_list(ll.reverseList(linked_list))