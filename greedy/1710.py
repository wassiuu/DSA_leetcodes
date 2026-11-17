'''
You are assigned to put some amount of boxes onto 
one truck. You are given a 2D array boxTypes, where
boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each 
box of the type i.
You are also given an integer truckSize, which is 
the maximum number of boxes that can be put on the 
truck. You can choose any boxes to put on the truck 
as long as the number of boxes does not exceed 
truckSize.

Return the maximum total number of units that can be 
put on the truck.

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
'''

class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda b: b[1], reverse=True)
        total = 0
        for box in boxTypes:
            print(box[0],box[1])
            if truckSize - box[0] >= 0:
                total += box[0] * box[1]
                truckSize -= box[0]
            else:
                while truckSize - box[0] < 0:
                    box[0] -= 1
                total += box[0] * box[1]
                return total
        return total 