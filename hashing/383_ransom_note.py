'''
Given two strings ransomNote and magazine, return true if 
ransomNote can be constructed by using the letters from 
magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mag = {}
        rans = {}

        for c in ransomNote:
            rans[c] = rans.get(c,0) + 1
        for c in magazine:
            mag[c] = mag.get(c,0) + 1

        for k,v in rans.items():
            if k in mag:
                if v > mag[k]:
                    return False
            else:
                return False
        return True



'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
            
        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False

        return True
'''

'''
# ---------------------------------------------------------------
# LC 383 - Ransom Note: notes (solved on my own!)
# ---------------------------------------------------------------
# IDEA: Count letters in both strings. The note can be built if
#       the magazine has AT LEAST as many of every letter it needs.
#
# STEPS:
#   1) Count each char in ransomNote -> rans
#   2) Count each char in magazine   -> mag
#   3) For each (letter, needed) in rans:
#        letter missing from mag, or mag[letter] < needed -> False
#   4) Every letter is covered -> True
#
# SHORTER CHECK: if mag.get(k, 0) < v: return False
#   (a missing letter counts as 0, so the if/else isn't needed)
#
# TESTS:
#   "a",  "b"   -> False
#   "aa", "ab"  -> False  (needs two a's, magazine has one)
#   "aa", "aab" -> True
#
# COMPLEXITY: O(n + m) time, O(1) space (only 26 letters)
#
# ONE-LINER ALTERNATIVE:
#   from collections import Counter
#   return not (Counter(ransomNote) - Counter(magazine))
# ---------------------------------------------------------------
'''