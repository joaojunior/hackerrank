from typing import List


class Solution():
    ZERO = 0
    ONE = 1
    TWO = 2

    def find_order(self, num_courses: int,
                   prerequisites: List[List[int]]) -> int:
        self.graph = {}
        for dest, source in prerequisites:
            if source in self.graph:
                self.graph[source].append(dest)
            else:
                self.graph[source] = [dest]

        self.colors = {}
        for node in range(num_courses):
            self.colors[node] = self.ZERO

        self.result = []
        for node in range(num_courses):
            if self.visit(node) is False:
                return []
        return self.result

    def visit(self, node):
        if self.colors[node] == self.TWO:
            return True
        if self.colors[node] == self.ONE:
            return False
        self.colors[node] = self.ONE
        for m in self.graph.get(node, []):
            result = self.visit(m)
            if result is False:
                return False
        self.colors[node] = self.TWO
        self.result.insert(0, node)
        return True


if __name__ == '__main__':
    solution = Solution()
    num_courses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(solution.find_order(num_courses, prerequisites))
