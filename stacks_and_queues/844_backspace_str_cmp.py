'''
Given two strings s and t, return true if they are equal 
when both are typed into empty text editors. '#' means a 
backspace character.

Note that after backspacing an empty text, the text will 
continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
'''

def backspaceCompare(s, t):
        stack_s = []
        stack_t = []

        for c in s:
            if c != "#":
                stack_s.append(c)
            elif stack_s:
                stack_s.pop()
            else:
                stack_s = stack_s
        
        for ch in t:
            if ch != "#":
                stack_t.append(ch)
            elif stack_t:
                stack_t.pop()
            else:
                stack_t = stack_t
        
        return "".join(stack_s) == "".join(stack_t)

'''
solution # 2:

    def backspaceCompare(s, t):
  
        def remove_characters(s):
            stack = []
            for char in s:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack

        return remove_characters(s) == remove_characters(t)
'''