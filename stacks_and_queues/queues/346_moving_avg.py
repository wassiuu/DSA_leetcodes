'''
Given a stream of integers and a window size, 
calculate the moving average of all integers 
in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object 
with the size of the window size.
double next(int val) Returns the moving average of 
the last size values of the stream.
 

Example 1:
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
'''

class MovingAverage(object):
  
    def __init__(self, size):
        self.s = size
        self.q = deque()
        self.counter = 0

    def next(self, val):
        self.sum = 0
        self.counter += 1
        self.q.append(val)
        if self.counter > self.s:
            self.counter -= 1
            self.q.popleft()
        for i in range(len(self.q)):
            self.sum += self.q[i]
        
        return float(self.sum)/self.counter