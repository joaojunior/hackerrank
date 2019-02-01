class Solution:
    def three_sum(self, nums):
        self.nums = sorted(nums)
        self.size = len(self.nums)
        self.result = []

        for i in range(self.size):
            self.find_sum(i)
        return self.result

    def find_sum(self, i):
        for j in range(i + 1, self.size):
            k = self.binary_search_tree(
                0 - (self.nums[j] + self.nums[i]), j + 1, self.size - 1
            )
            if k != -1:
                self.result.append([self.nums[i], self.nums[j], self.nums[k]])
                return

    def binary_search_tree(self, value, l, r):
        if r < l:
            return -1
        else:
            mid = l + (r - l) // 2
            if self.nums[mid] == value:
                return mid
            elif self.nums[mid] > value:
                return self.binary_search_tree(value, l, mid - 1)
            else:
                return self.binary_search_tree(value, mid + 1, r)


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print(solution.three_sum(nums))
