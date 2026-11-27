'''
Given a pattern and a string s, find if s follows the same 
pattern.

Here follow means a full match, such that there is a 
bijection between a letter in pattern and a non-empty 
word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to 
the same letter.
 

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanatio
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
'''

class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split(" ")
        map_to_s = {}
        map_to_p = {}

        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            c = pattern[i]
            if c in map_to_s:
                if map_to_s[c] != words[i]:
                    return False
            else:
                if words[i] in map_to_p:
                    return False
                else:
                    map_to_s[c] = words[i]
                    map_to_p[words[i]] = c
        return True

'''
# ---------------------------------------------------------------
# LC 290 - Word Pattern: notes (solved on my own!)
# ---------------------------------------------------------------
# IDEA: Same as LC 205 (Isomorphic Strings), except pattern
#       letters map to whole WORDS instead of single characters.
#   map_to_s: pattern-char -> word
#   map_to_p: word -> pattern-char
#
# STEP 0: Split s into words. If len(words) != len(pattern),
#         return False right away (a 1-to-1 mapping is impossible).
#
# AT EACH INDEX i (c = pattern[i], w = words[i]):
#   1) c seen before (c in map_to_s):
#        It must map to the SAME word as before.
#        Check: map_to_s[c] == w. If not -> return False.
#   2) c is new:
#        If w is already in map_to_p, a DIFFERENT pattern char
#        already took this word -> return False.
#        Otherwise record both directions:
#          map_to_s[c] = w
#          map_to_p[w] = c
#
# WHY TWO MAPS: one map only catches "one letter -> two words".
#   The second map catches "two letters -> the same word".
#   e.g. pattern="ab", s="dog dog" needs map_to_p to fail.
#
# KEY CHECK: compare the stored value to the CURRENT word
#   (map_to_s[c] != words[i]), not to a lookup in the other map.
#
# TIP: s.split() (no argument) is more robust than s.split(" ").
#
# TESTS:
#   "abba", "dog cat cat dog"  -> True
#   "abba", "dog cat cat fish" -> False  (a maps to dog and fish)
#   "aaaa", "dog cat cat dog"  -> False
#   "abba", "dog dog dog dog"  -> False  (a and b both map to dog)
#   "aaa",  "dog dog dog dog"  -> False  (length mismatch)
#
# COMPLEXITY: O(n + m) time, where m = length of s (for splitting)
#             O(number of unique words) space
#
# ONE-LINER ALTERNATIVE:
#   w = s.split()
#   return len(pattern) == len(w) and \
#          len(set(pattern)) == len(set(w)) == len(set(zip(pattern, w)))
# ---------------------------------------------------------------
'''