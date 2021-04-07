class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def insert_sort_list(self, head: ListNode) -> ListNode:
        p = head
        while p.next is not None:
            j = p.next
            if j.val <= head.val:
                p.next = p.next.next
                j.next = head
                head = j
            else:
                i = head
                while i.next != j and i.next.val < j.val:
                    i = i.next
                if i.next != j:
                    p.next = p.next.next
                    i.next, j.next = j, i.next
                else:
                    p = p.next
        return head
