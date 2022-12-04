from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ## Linked lists are a data pointer structure
        ## We check if list1 or list 2 is empty first and return pointer to other ll
        ## assign current/dummy linked list
        ## while both are not empty check vals
        ## if l1 val < l2 val, update current pointer to lower val list
        ## update list to listx.next to iterate through
        ## if any become empty, simply add next val == to non empty ll
        ## return dummy node since that is the beginning (head)

        if not list1: return list2
        if not list2: return list1

        current = head = ListNode()

        while list1 and list2:

            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return head.next
