from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, new = None, head

        while new:
            temp = new.next
            new.next = prev
            prev = new
            new = temp

        return prev

if __name__ == '__main__':

    list1 = ListNode(1)
    list2 = ListNode(2)
    list3 = ListNode(3)

    list1.next = list2
    list2.next = list3
    head = Solution().reverseList(list1)

    output = []

    while head:
        output.append(head.val)
        head = head.next

    print(output)