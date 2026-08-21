'''
Given a string s, sort it in decreasing order based 
on the frequency of the characters. The frequency of a 
character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, 
return any of them.

 

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

def frequencySort(self, s):
        freq = {}
        sorted = ""
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        char_map = {}
        for key in freq:
          if freq[key] in char_map:
              char_map[freq[key]].append(key)
          else:
              char_map[freq[key]] = [key]

        "max frequency keys will always be greater than 0 and less than len(s)"
        for i in range(len(s),0,-1):
            if i in char_map:
                for char in char_map[i]:
                    sorted += char * i
        return sorted

            