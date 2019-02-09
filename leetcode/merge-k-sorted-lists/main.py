from typing import List


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.root = None
        self.merge(lists, self.root)
        return self.root

    def merge(self, lists: List[ListNode], root: ListNode):
        small = 10**10
        idx = -1
        for i, _list in enumerate(lists):
            if _list and _list.val < small:
                small = _list.val
                idx = i
        if idx != -1:
            if self.root is None:
                self.root = ListNode(lists[idx].val)
                root = self.root
            else:
                root.next = ListNode(lists[idx].val)
                root = root.next
            if lists[idx].next is not None:
                lists[idx] = lists[idx].next
            else:
                lists.pop(idx)
            if lists:
                self.merge(lists, root)
