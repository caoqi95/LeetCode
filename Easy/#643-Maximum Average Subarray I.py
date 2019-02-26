"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the 
maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 

Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum = list(range(len(nums)))
        sum[0] = nums[0]
        # 计算累加的和
        for i in range(1, len(nums)):
            sum[i] = sum[i-1] + nums[i]
        
        res = float(sum[k-1]*1.0 / k)
        # 计算不同 k 位的均值
        for i in range(k, len(nums)):
            res = max(res, (sum[i] - sum[i-k])*1.0/k)
        
        return res



if __name__ == "__main__":

    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    solution = Solution()
    print(solution.findMaxAverage(nums, k))