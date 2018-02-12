import math


class PrimeDigitSums():
    def prime_digit_sums(self, digits):
        first = 10 ** (digits - 1)
        last = 10 ** digits - 1
        self.memoize = {}
        result = 0
        for number in range(first, last):
            consecutives = consecutive(number, 3)
            prime = self.all_numbers_are_prime(consecutives)

            if prime is True:
                consecutives = consecutive(number, 4)
                prime = self.all_numbers_are_prime(consecutives)

            if prime is True:
                consecutives = consecutive(number, 5)
                prime = self.all_numbers_are_prime(consecutives)

            if prime is True:
                result += 1
        return result

    def all_numbers_are_prime(self, numbers):
        for number in numbers:
            if number not in self.memoize:
                self.memoize[number] = is_prime(number)
            if self.memoize[number] is False:
                return False
        return True


def consecutive(number, size):
    number_str = str(number)
    result = []
    i = 0
    while i + size <= len(number_str):
        n = 0
        for j in range(size):
            n += int(number_str[i + j])
        result.append(n)
        i += 1
    return result


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    i = 3
    sqrt = math.sqrt(number)
    while i <= sqrt:
        if number % i == 0:
            return False
        i += 2
    return True


if __name__ == '__main__':
    quantity = int(input())
    for i in range(quantity):
        prime = PrimeDigitSums()
        digits = int(input())
        print(prime.prime_digit_sums(digits))
