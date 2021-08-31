class Solution:
    def count_good_numbers(self, n: int) -> int:
        result = 1
        even_digits = 5
        prime_numbers = 4
        large = 1000000007
        q, r = divmod(n, 2)
        result = pow(even_digits, q + r, large) * pow(prime_numbers, q, large)
        return result % large
