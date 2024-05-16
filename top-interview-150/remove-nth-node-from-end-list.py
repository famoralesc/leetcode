from typing import Optional
from utils.types import ListNode

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    """
    pos = 1
    first = head
    while head:
        head.pos = pos
        head = head.next
        pos += 1
    newHead = None
    while first:
        if first.pos == pos - n: 
            pass
        else:
            newNode = ListNode(val = first.val)
            if not newHead:
                newHead = newNode
            else:
                curr = newHead
                while curr.next:
                    curr = curr.next
                curr.next = newNode          
        first = first.next    
    return newHead