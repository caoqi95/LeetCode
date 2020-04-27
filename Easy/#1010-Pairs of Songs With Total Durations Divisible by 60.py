"""
n a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. 
Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Note:

1 <= time.length <= 60000
1 <= time[i] <= 500
"""
from collections import defaultdict

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        
        """
        # my solution - Time Limit Exceeded
        count = 0
        new_time = time.copy()
        for i in range(len(time) - 1):
            new_time.remove(time[i])
            for j in range(len(new_time)):
                if (time[i] + new_time [j]) % 60 == 0:
                    count += 1
        return count
        """
        # other's solution
        cnt, lookup = 0, defaultdict(int)
        for t in time:
            have = t % 60
            if have == 0:
                need = 0
            else:
                need = 60 - have
            
            cnt += lookup[need]
            lookup[have] += 1
        
        return cnt
        
if __name__ == "__main__":

    # time = [30, 20, 150, 100, 40]
    time = [60, 60, 60]
    solution = Solution()
    print(solution.numPairsDivisibleBy60(time))
