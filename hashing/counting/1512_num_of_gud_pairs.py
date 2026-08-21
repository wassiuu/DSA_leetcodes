'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0
'''

def numIdenticalPairs(nums):
        ans = 0
        freq = {}
        for num in nums:
            if num in freq:
                ans += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1
        return ans

'''
basically each time a number has appeared previously, it can form a good pair with all of its 
previous occurrences. 
So we can keep track of the frequency of each number and add that frequency to the answer 
each time we encounter that number again.
'''

