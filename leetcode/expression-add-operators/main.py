from typing import List


class Solution:
    def add_operators(self, num: str, target: int) -> List[str]:
        if num == "":
            return []
        self.nums = num
        self.result = []
        self.target = target
        self.operation(0, 0, [], 0)
        return self.result

    def operation(self, index, value, ops, last):
        if index < len(self.nums):
            current_val = 0
            i = index
            start_with_zero = False
            while i < len(self.nums) and start_with_zero is False:
                current_val = current_val*10 + int(self.nums[i])
                if index == 0:
                    self.operation(i + 1, current_val, ops+[str(current_val)],
                                   current_val)
                else:
                    v = value - last
                    self.operation(i + 1, v+(last*current_val),
                                   ops+['*'+str(current_val)],
                                   last*current_val)
                    self.operation(i + 1, value+current_val,
                                   ops+['+'+str(current_val)], current_val)
                    self.operation(i + 1, value-current_val,
                                   ops+['-'+str(current_val)], -current_val)
                if self.nums[index] == '0':
                    start_with_zero = True
                i += 1
        else:
            if value == self.target:
                self.result.append(''.join(ops))


if __name__ == '__main__':
    solution = Solution()
    num = '105'
    target = 5
    print(solution.add_operators(num, target))
