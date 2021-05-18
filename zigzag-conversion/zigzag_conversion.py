class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        lines = []
        for row in range(num_rows):
            lines.append([])
        i = 0
        increment = 1
        for c in s:
            lines[i].append(c)
            if i == 0:
                increment = 1
            elif i + 1 == num_rows:
                increment = -1
            i += increment
            if i >= num_rows:
                i = 0
        result = ''
        for line in lines:
            result += ''.join(line)
        return result
