'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "Mr Ding"
Output: "rM gniD"
'''

def reverseWords(s):
        s_arr = list(s)
        l = 0
        for r in range(len(s_arr)):
            if s_arr[r] == " " or r == len(s_arr)-1:
                temp_l = l
                temp_r = r - 1
                if r == len(s_arr)-1:
                    temp_r = r
                while temp_l < temp_r:
                    s_arr[temp_l], s_arr[temp_r] = s_arr[temp_r], s_arr[temp_l]
                    temp_l += 1
                    temp_r -= 1
                l = r+1
        return "".join(s_arr)