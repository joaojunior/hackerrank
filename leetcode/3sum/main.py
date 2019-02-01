class Solution:
    def three_sum(self, nums):
        self.nums = sorted(nums)
        self.size = len(self.nums)
        self.result = []

        for i in range(self.size):
            self.find_sum(i)
        return self.result

    def find_sum(self, i):
        value = 0 - self.nums[i]
        j = i + 1
        k = self.size - 1
        while j < k:
            if self.nums[j] + self.nums[k] == value:
                r = [self.nums[i], self.nums[j], self.nums[k]]
                if r not in self.result:
                    self.result.append(r)
                j += 1
                k -= 1
            elif self.nums[j] + self.nums[k] > value:
                k -= 1
            else:
                j += 1


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print(solution.three_sum(nums))
    print(solution.three_sum([-2, 0, 1, 1, 2]))
