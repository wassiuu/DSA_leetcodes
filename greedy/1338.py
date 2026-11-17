'''
You are given an integer array arr. 
You can choose a set of integers and remove 
all the occurrences of these integers in the array.

Return the minimum size of the set so that at least 
half of the integers of the array are removed.


Example 1:
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
'''

class Solution(object):
    def minSetSize(self, arr):
        freq = {}
        half = len(arr)//2
        length = len(arr)
        count = 1 
        for num in arr:
            freq[num] = freq.get(num,0)+1
        freqs = sorted(freq.values(), reverse=True)
        for f in freqs:
            if length - f > half:
                count += 1
                length = length - f
            else:
                return count 