class SamSubStrings():
    def calculate(self, number):
        self.numbers = []
        self.sum_ = 0
        for i in str(number):
            self.numbers.append(int(i))
        self.positions = list(range(len(self.numbers)))
        queue = []
        for position in self.positions:
            queue.append([position])
        while queue:
            substring = queue.pop(0)
            self.sum_ += self.transform_position_to_number(substring)
            if len(substring) < len(self.numbers):
                for i, number in enumerate(self.numbers):
                    if i == substring[-1] + 1:
                        queue.append(substring[:] + [i])
        return self.sum_ % (10**9 + 7)

    def transform_position_to_number(self, positions):
        result = ""
        for position in positions:
            result += str(self.numbers[position])
        return int(result)


if __name__ == "__main__":
    balls = input().strip()
    sam_sub_strings = SamSubStrings()
    result = sam_sub_strings.calculate(balls)
    print(result)
