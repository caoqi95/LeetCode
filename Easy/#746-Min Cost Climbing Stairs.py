"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to 
reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
    1. cost will have a length in the range [2, 1000].
    2. Every cost[i] will be an integer in the range [0, 999].
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        """
        p1, p2 = 0, 0
        for i in range(2, len(cost)+1):
            p1, p2 = p2, min(p2+cost[i-1], p1+cost[i-2])

        return p2
        """
        # solution 2
        if len(cost) == 2:
            return min(cost)

        for i in range(2, len(cost)):
            # 当前的 cost 值与前两个中最小的值累加，然后一直循环判断
            cost[i]  += min(cost[i-1], cost[i-2])
            #print(i, cost[i])
        
        return min(cost[-2], cost[-1])


if __name__ == "__main__":

    # cost = [10, 15, 20]  # return 15
    # cost = [0, 0, 0, 0]  # reurn 0
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]  # return 6
    solution = Solution()
    print(solution.minCostClimbingStairs(cost))