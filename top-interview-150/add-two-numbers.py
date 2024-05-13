from typing import Optional
from utils.types import ListNode

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """
    l1String = ""
    while l1 is not None:
        l1String = str(l1.val)+l1String
        l1 = l1.next
    
    l2String = ""
    while l2 is not None:
        l2String = str(l2.val)+l2String
        l2 = l2.next
    l1Number = int(l1String)
    l2Number = int(l2String)
    number = str(l1Number + l2Number)
    i = len(number) -1 
    head = None
    while i>=0:
        node = ListNode(val = number[i])
        if head is None:
            head = node
        else:
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = node
        i -= 1
    return head