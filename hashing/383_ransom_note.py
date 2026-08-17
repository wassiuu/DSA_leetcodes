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
def canConstruct(ransomNote, magazine):
        mag_dic = {}
        flag = False
        for char in magazine:
            if char in mag_dic:
                mag_dic[char] += 1
            else:
                mag_dic[char] = 1
        for char in ransomNote:
            if char in mag_dic and mag_dic[char] > 0:
                mag_dic[char] -= 1
                flag = True
            else:
                return False
        return flag
