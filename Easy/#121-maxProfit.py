"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or not prices or len(prices) == 1:
            return 0

        else:
            maxi = mini = prices[0]
            diff = 0

            for i in range(0, len(prices)):
                # 如果大于 maxi ，则替换最大值
                if prices[i] > maxi:
                    maxi = prices[i]
                    if (maxi - mini) > diff:
                        diff = maxi - mini
                # 如果小于 mini，则最大值最小值替换成一样的值，
                # 即变成一样的起点，且 diff 保持不变
                if prices[i] < mini:
                    mini = maxi = prices[i]

            return diff


if __name__ == '__main__':

    prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 6, 5, 3, 1]
    # prices = [2, 4, 1]
    solution = Solution()
    solution.maxProfit(prices)