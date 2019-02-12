convert = {
    0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
    7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven',
    12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
    16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
    20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
    70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'Hundred'}
special = {0: 'Zero', 1000000: 'One Million'}


class Solution:
    def number_to_words(self, num: int) -> str:
        if num in special:
            return special[num]
        result = []
        pot = ['Thousand', 'Million', 'Billion']
        while num > 0:
            q, r = num // 1000, num % 1000
            if r != 0:
                parcial = self.convert(r)
                if parcial:
                    result = parcial + result
            num = q
            if num > 0:
                result.insert(0, pot.pop(0))
        return ' '.join(result)

    def convert(self, n: int) -> str:
        q, r = n // 100, n % 100
        result = []
        if q > 0:
            result.append(convert[q])
            result.append('Hundred')
        if r > 0:
            if r < 20 or r % 10 == 0:
                result.append(convert[r])
            else:
                q1, r = r // 10, r % 10
                result.append(convert[q1*10])
                result.append(convert[r])
        return result


if __name__ == '__main__':
    solution = Solution()
    num = 20
    print(solution.number_to_words(num))
