'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is 
"dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is 
"a", whose length is 1.
'''

class Solution(object):
    def longestPalindrome(self, s):
        ans = 0 
        remain = False
        freq = {}
        for c in s:
            freq[c] = freq.get(c,0) + 1
    
        for c in freq.values():
            if c%2 == 0:
                ans += c
            else:
                ans += (c - c%2)
                remain = True
        return ans + 1 if remain else ans 

# ---------------------------------------------------------------
# LC 409 - Longest Palindrome: notes + interview guide
# ---------------------------------------------------------------
# PROBLEM (clearer version):
#   Rearrange any of the letters in s to build the longest
#   palindrome you can, and return its LENGTH.
#
# CLARIFYING QUESTIONS (ask in an interview):
#   - Can I rearrange freely?          -> yes (NOT a substring problem)
#   - Must I use every letter?         -> no
#   - Case-sensitive?                  -> yes, 'a' != 'A'
#   - Return the string or the length? -> length only
#
# KEY OBSERVATION (say this before coding):
#   "A palindrome is mirrored, so every letter needs a partner on
#    the other side, except one letter that can sit in the middle.
#    So the answer is all the pairs I can make, plus 1 if any
#    letter is left over."
#
# APPROACH:
#   1) Count each letter's frequency with a hash map.
#   2) For each count:
#        even -> use all of it
#        odd  -> use count - 1 (the even part), set remain = True
#   3) After the loop, if remain: add 1 (one center letter only).
#
#   Interview version: "I count frequencies, take the even part
#   of every count, and add 1 at the end if any count was odd."
#
# EXAMPLE WALKTHROUGH ("bananas"):
#   Counts: a:3, n:2, b:1, s:1
#   Even parts: 2 + 2 + 0 + 0 = 4
#   There are odd counts, so +1 for the center -> 5   (e.g. "naaan")
#
# MISTAKES I MADE:
#   - Added the FULL odd count (a×3 -> 3) and then +1 for another
#     single letter. That's two unpaired letters, which is
#     impossible because there's only one middle.
#     "bananas" gave 6, should be 5.
#   - Only treated freq == 1 as odd. Any odd count leaves a
#     leftover: "aaa" -> 3.
#   - Sorted the counts for no reason. Order doesn't matter.
#   - Misread LeetCode: "Output" = MY code, "Expected" = correct.
#
# USEFUL OPERATORS:
#   c % 2          -> remainder (0 = even, 1 = odd)
#   c - c % 2      -> largest even number <= c
#   c // 2 * 2     -> same thing, using floor division
#
# EDGE CASES (mention these):
#   "a"   -> 1   (a single letter is a palindrome)
#   "abc" -> 1   (no pairs, one center)
#   "aA"  -> 1   (case matters)
#   "aabb"-> 4   (all even, no +1)
#
# COMPLEXITY:
#   Time:  O(n) (one pass to count, one pass over counts)
#   Space: O(1) (at most 52 distinct letters)
#
# ALTERNATIVE (if asked):
#   Use a set: add a letter when you see it, and remove it when you
#   see it again, adding 2 to the answer each time you remove one.
#   At the end, add 1 if the set isn't empty.
# ---------------------------------------------------------------