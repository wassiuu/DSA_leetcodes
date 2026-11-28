'''
Given a list of dominoes, dominoes[i] = [a, b] is 
equivalent to dominoes[j] = [c, d] if and only if either 
(a == c and b == d), or (a == d and b == c) - that is, 
one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for 
which 0 <= i < j < dominoes.length, and dominoes[i] is 
equivalent to dominoes[j].

Example 1:
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

Example 2:
Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
'''


class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        seen = {}
        count = 0
        for d in dominoes:
            key = (min(d),max(d))
            if key in seen:
                count += seen[key]
                seen[key] += 1
            else:
                seen[key] = seen.get(key,0) + 1
        
        return count


"""
Number of Equivalent Domino Pairs

Idea:
- Two dominoes are equal if they have the same two numbers in any order,
  so [1,2] == [2,1]. Normalize each domino so equal ones get the same key.
- Count PAIRS, not duplicates. A new domino forms a pair with EVERY
  identical domino seen before it (like a newcomer shaking hands with
  everyone already in the room).

How it works:
- seen[key] = how many times this domino has appeared so far.
- For each domino:
    1. count += seen[key]   -> new pairs this domino makes with earlier ones
    2. seen[key] += 1       -> now record this domino
  (Order matters: add to count BEFORE increasing the tally.)
- Each pair is counted exactly once, when its second domino shows up.
- One shared `count` for all domino types; each type has its own tally.
- Check: k identical dominoes give 0+1+...+(k-1) = k*(k-1)/2 pairs.

Making the key (two options):
- key = tuple(sorted(d))
    sorted(d) returns a NEW sorted list (d.sort() sorts in place and
    returns None, so it can't be chained). tuple() makes it hashable,
    because lists can't be dict keys.
- key = (min(d), max(d))
    Works because each domino has exactly 2 numbers. Same result,
    slightly faster since no list is built.

Complexity: O(n) time, O(n) space.
"""
