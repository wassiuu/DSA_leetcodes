'''
Given a string s, reverse the string according to the 
following rules:

All the characters that are not English letters remain in 
the same position.
All the English letters (lowercase or uppercase) should 
be reversed. Return s after reversing it.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
'''

def reverseOnlyLetters(s):
        s = list(s)
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalpha():
                l+=1
            elif not s[r].isalpha():
                r-=1
            else:
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1
        return "".join(s)