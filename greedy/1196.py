'''
You have some apples and a basket that can carry 
up to 5000 units of weight.

Given an integer array weight where weight[i] 
is the weight of the ith apple, return the maximum 
number of apples you can put in the basket.

 

Example 1:
Input: weight = [100,200,150,1000]
Output: 4
Explanation: All 4 apples can be carried by the 
basket since their sum of weights is 1450.
'''

class Solution(object):
    def maxNumberOfApples(self, weight):
        weight.sort()
        total = 0
        count = 0
        for w in weight:
            if total + w <= 5000:
                count += 1
                total += w
            else:
                break
        return count