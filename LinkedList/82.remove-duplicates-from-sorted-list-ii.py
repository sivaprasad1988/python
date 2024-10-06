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
listRecords = [1,2,3,3,4,4,5]

linked_list = create_linked_list(listRecords)

#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        dummy = head
        result = ListNode(0)

        while current is not None:
            count = 0
            while dummy is not None:
                if current.val == dummy.val:
                    count += 1
                if dummy.next is None:
                    if count == 1:
                        newNode = ListNode(current.val)
                        newNode.next = result.next
                        result.next = newNode
                dummy = dummy.next
            else:
                dummy = head

            current = current.next

        headNewResult = result.next
        currentResult = headNewResult
        previous = None


        while headNewResult is not None:
            next = headNewResult.next
            headNewResult.next = previous
            previous = headNewResult
            headNewResult=next

        headNewResult = previous

        return headNewResult

ll = Solution()
print_linked_list(ll.deleteDuplicates(linked_list))