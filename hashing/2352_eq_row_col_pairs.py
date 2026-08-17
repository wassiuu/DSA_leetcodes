'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) 
such that row ri and column cj are equal.

A row and column pair is considered equal if they contain 
the same elements in the same order (i.e., an equal array).

Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
'''

def equalPairs(grid):
        def convert_to_key(arr):
            return tuple(arr)

        dic = {}

        # Count rows
        for row in grid:
            key = convert_to_key(row)

            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1

        dic2 = {}

        # Count columns
        for col in range(len(grid[0])):
            current_col = []

            for row in range(len(grid)):
                current_col.append(grid[row][col])

            key = convert_to_key(current_col)

            if key in dic2:
                dic2[key] += 1
            else:
                dic2[key] = 1

        ans = 0

        # Check which rows also exist as columns
        for arr in dic:
            if arr in dic2:
                ans += dic[arr] * dic2[arr]

        return ans