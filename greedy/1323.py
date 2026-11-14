'''
You are given a positive integer num consisting 
only of digits 6 and 9.

Return the maximum number you can get by changing
at most one digit (6 becomes 9, and 9 becomes 6).
'''

class Solution(object):
    def maximum69Number (self, num):
        digits = [int(d) for d in str(num)]
        for i in range(len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                break          # only one change allowed
        return int("".join(map(str, digits)))
            