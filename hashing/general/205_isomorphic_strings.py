'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s 
can be replaced to get t.

All occurrences of a character must be replaced with another 
character while preserving the order of characters. No two 
characters may map to the same character, but a character may 
map to itself.


Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "f11", t = "b23"
Output: false
Explanation:
The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:
Input: s = "paper", t = "title"
Output: true
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        hash_s = {}
        hash_t = {}

        for i in range(len(s)):
            c = s[i]
            if c in hash_s:
                if hash_s[c] != t[i]:
                    return False
            else:
                hash_s[c] = t[i]
                if t[i] in hash_t:
                    return False
                else:
                    hash_t[t[i]] = c
        return True


'''
# ---------------------------------------------------------------
# LC 205 - Isomorphic Strings: notes
# ---------------------------------------------------------------
# IDEA: Use two dicts to keep the mapping one-to-one, both ways.
#   hash_s: s-char -> t-char
#   hash_t: t-char -> s-char
#
# AT EACH INDEX i (c = s[i]):
#   1) c seen before (c in hash_s):
#        It must map to the SAME t-char as before.
#        Check: hash_s[c] == t[i]. If not -> return False.
#   2) c is new:
#        If t[i] is already in hash_t, some OTHER s-char already
#        took it -> return False (two s-chars can't share one t-char).
#        Otherwise record both directions:
#          hash_s[c] = t[i]
#          hash_t[t[i]] = c
#
# MISTAKES I MADE:
#   - hash_s[c] != hash_t[c]
#       c is an s-char, so it doesn't belong as a key in hash_t.
#       Don't mix up the two dicts' key types.
#   - hash_s[c] != hash_t[t[i]]
#       This compares a t-char to an s-char, which never makes sense.
#       It also raises a KeyError if t[i] isn't in hash_t yet.
#       Counterexample: s="aba", t="bab" -> returns False (should be True)
#   - Right check: hash_s[c] != t[i]  (compare to the CURRENT t-char)
#
# TIP: Name the dicts s_to_t / t_to_s so it's obvious what each
#      key and value are.
#
# TESTS:
#   "egg", "add"   -> True
#   "foo", "bar"   -> False  (o maps to both a and r)
#   "badc", "baba" -> False  (b and d both map to b)
#   "aa", "ab"     -> False
#
# COMPLEXITY: O(n) time, O(1) space (the alphabet is bounded)
#
# ONE-LINER ALTERNATIVE:
#   return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
# ---------------------------------------------------------------
'''