class Solution:
    def find_the_winner(self, n: int, k: int) -> int:
        players = []
        for i in range(n):
            players.append(i+1)
        start = 0
        while len(players) > 1:
            size = len(players)
            i = (start + k - 1) % size
            players.pop(i)
            start = i

        return players[0]
