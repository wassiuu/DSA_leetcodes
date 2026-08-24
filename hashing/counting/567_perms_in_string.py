'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''

def checkInclusion(s1, s2):
        freq1 = {}
        freq2 = {}
        l = r = 0
        for char in s1:
            freq1[char] = freq1.get(char,0)+1
        
        for r in range(len(s2)):
            char = s2[r]
            freq2[char] = freq2.get(char,0)+1
            if (r-l+1) == len(s1):
                if freq1 == freq2:
                    return True 
                else:
                    freq2[s2[l]] -= 1
                    if freq2[s2[l]] == 0:
                        del freq2[s2[l]]
                    l += 1
        return False

'''
fixed sized sliding window + hashmap freq counting of the chars in each window
'''