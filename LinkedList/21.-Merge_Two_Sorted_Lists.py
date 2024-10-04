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
        print(current.val, end="=>")
        current = current.next


list1 = create_linked_list([])
list2 = create_linked_list([])




class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sortedFinalList = []
        newSortedArray = []
        while list1 is not None:
            sortedFinalList.append(list1.val)
            list1 = list1.next

        while list2 is not None:
            sortedFinalList.append(list2.val)
            list2 = list2.next

        n = len(sortedFinalList)
        if n >0:
            for i in range(n):
                for j in range(0, n - i - 1):
                    if sortedFinalList[j] > sortedFinalList[j + 1]:
                        # Swap elements if they are in the wrong order
                        sortedFinalList[j], sortedFinalList[j + 1] = sortedFinalList[j + 1], sortedFinalList[j]

            head = ListNode(sortedFinalList[0])
            current = head
            for val in sortedFinalList[1:]:
                current.next = ListNode(val)
                current = current.next
        else:
            head = ListNode('')

        return head


s = Solution()
print_linked_list(s.mergeTwoLists(list1,list2))
