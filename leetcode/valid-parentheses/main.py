class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        lookup_table = {'{': '}', '[': ']', '(': ')'}
        for c in s:
            if c in lookup_table:
                stack.append(c)
            else:
                if not stack or c != lookup_table.get(stack.pop(), None):
                    return False
        return not stack
