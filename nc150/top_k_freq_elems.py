'''
Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the 
answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        print(freq)

        buckets = [[] for _ in range(len(nums) + 1)]
        print(buckets)

        for key,v in freq.items():
            count = freq[key]
            buckets[count].append(key)
        
        print(buckets)

        for i in range(len(buckets)-1,0,-1):
            for b in buckets[i]:
                if len(result) == k:
                    return result
                else:
                    result.append(b)
        return result