class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.head = ListNode(0)
        self.add(l1, l2, self.head)
        return self.head

    def add(self, root1: ListNode, root2: ListNode,
            result: ListNode) -> ListNode:
        if root1 is not None:
            result.val += root1.val
            root1 = root1.next
        if root2 is not None:
            result.val += root2.val
            root2 = root2.next
        if result.val > 9:
            result.next = ListNode(1)
            result.val = result.val-10
            self.add(root1, root2, result.next)
        else:
            if root1 is not None or root2 is not None:
                result.next = ListNode(0)
                self.add(root1, root2, result.next)
