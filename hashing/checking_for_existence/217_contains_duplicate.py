'''
Given an integer array nums, return true if any value 
appears at least twice in the array, and return false 
if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

def containsDuplicate(nums):
        numbers = {}
        flag = False
        for num in nums:
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1
        for value in numbers.values():
            if value > 1:
                flag = True
        return flag

"a better solution:"

'''
def containsDuplicate(nums):
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False
'''