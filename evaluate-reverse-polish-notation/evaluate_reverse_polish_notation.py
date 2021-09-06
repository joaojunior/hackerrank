from typing import List


class Solution:
    def eval_rpn(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for i in tokens:
            if i in operators:
                n1, n2 = stack.pop(), stack.pop()
                result = 0
                if i == '+':
                    result = n2 + n1
                elif i == '-':
                    result = n2 - n1
                elif i == '*':
                    result = n2 * n1
                else:
                    result = int(n2 / n1)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack.pop()
