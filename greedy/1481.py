'''
Given an array of integers arr and an integer k. 
Find the least number of unique integers 
after removing exactly k elements.
'''

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        count = {}
        removed = 0
        for num in arr:
            count[num] = count.get(num,0) + 1

        print(count)
        
        sorted_counts = sorted(count.values())

        print(sorted_counts)
        for c in sorted_counts:
            if k >= c:
                k -= c
                removed += 1
        return len(count) - removed