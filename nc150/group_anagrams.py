class Solution(object):
    def groupAnagrams(self, strs):
        strings = {}
        result = []
        for s in strs:
            y = "".join(sorted(s))
            if y in strings:
                strings[y].append(s)
            else:
                strings[y] = [s]
        
        for v in strings.values():
            result.append(v)
        
        return result