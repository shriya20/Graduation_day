import pytest
import math
import unittest


class graduation:
    def __init__(self, days, ways, ways_he_miss, res) -> None:
        self.days = days
        self.ways = ways
        self.ways_he_miss = ways_he_miss
        self.res = res

    def calculateMissWays(self):

        extra = 0
        for i in range(int(math.pow(2, self.days))):
            num = format(i, "b")
            num = str(num)
            zero_filled_number = num.zfill(self.days)
            substr = '0000'
            if substr in zero_filled_number:
                self.ways += 1
            if substr in zero_filled_number and zero_filled_number.endswith('0'):
                extra += 1
            elif zero_filled_number.endswith('0'):
                self.ways_he_miss += 1

    def calculate_result(self):
        if self.days == 1:
            a1 = 0
            a1 = '1/2'
            self.res = '1/2'
        elif self.days == 2:
            self.res = '1/2'
        elif self.days == 3:
            self.res = '1/2'
        else:
            total_ways = pow(2, self.days)
            total_ways = total_ways-self.ways
            self.res = str(self.ways_he_miss)+'/'+str(total_ways)


class testing_purpose:
    def __init__(self, days, ways, ways_he_miss, res) -> None:
        self.days = days
        self.ways = ways
        self.ways_he_miss = ways_he_miss
        self.res = res

    def test_method(self):
        grad = graduation(self.days, self.ways, self.ways_he_miss, self.res)
        return grad


if __name__ == "__main__":
    print("Enter the number of days")
    n = int(input())
    res = ''
    grad = graduation(n, 0, 0, res)
    l = grad.calculateMissWays()
    grad.calculate_result()
    print(grad.res)
