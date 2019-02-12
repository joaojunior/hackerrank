convert = {
    0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
    7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven',
    12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
    16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
    20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
    70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'Hundred',
    1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'}


class Solution:
    def number_to_words(self, num: int) -> str:
        result = []
        pot = ['Thousand', 'Million', 'Billion']
        while num > 0:
            q, r = num // 1000, num % 1000
            if r != 0:
                parcial = self.convert(r)
                if parcial:
                    result.append(parcial)
            num = q
            if num > 0:
                result.append(pot.pop(0))
        result.reverse()
        return ' '.join(result)

    def convert(self, n: int) -> str:
        q, r = n // 100, n % 100
        result = ''
        if q > 0:
            result += ' '.join([convert[q], 'Hundred'])
        if r < 20:
            result = ' '.join([result, convert[r]])
        else:
            q1, r = r // 10, r % 10
            result = ' '.join([result, convert[q1*10], convert[r]])
        return result


if __name__ == '__main__':
    solution = Solution()
    num = 1000010
    print(solution.number_to_words(num))
