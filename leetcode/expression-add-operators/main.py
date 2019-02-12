from typing import List


class Solution:
    def add_operators(self, num: str, target: int) -> List[str]:
        if num == "":
            return []
        self.result = []
        self.target = target
        self.operation(num[1:], [num[0]], int(num[0]))
        return self.result

    def operation(self, num, parcial, total):
        if num:
            digit = int(num[0])
            if digit + total <= self.target:
                self.operation(
                    num[1:], parcial[:] + ['+', num[0]], total + digit)
            if digit - total <= self.target:
                self.operation(
                    num[1:], parcial[:] + ['-', num[0]], total - digit)
            if digit * total <= self.target:
                self.operation(
                    num[1:], parcial[:] + ['*', num[0]], total * digit)
        else:
            if total == self.target:
                self.result.append(''.join(parcial))


if __name__ == '__main__':
    solution = Solution()
    num = '232'
    target = 8
    print(solution.add_operators(num, target))
