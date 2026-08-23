'''
Given a binary array nums and an integer goal, return the number 
of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15
'''

def numSubarraysWithSum(nums, goal):
        count = {}
        cum_sum = 0
        ans = 0
        count[cum_sum] = 1
        for num in nums:
            cum_sum += num 
            prev_sum = cum_sum-goal
            if prev_sum in count:
                ans += count[prev_sum]
            count[cum_sum] = count.get(cum_sum,0) + 1
        
        return ans

