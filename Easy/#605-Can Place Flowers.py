"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0 : return True

        j = 0 # position where next possible flower can be planted
        for i, e in enumerate(flowerbed):
            if e == 1:
                # next possible flower can be planted at i + 2 position only
                j = i + 2
                continue
            else:
                # it seems we can plant flower here, lets check it will conflict with
                # the possible flower in next cell
                if i == j and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                    n -= 1 # 1 more flower successfully planted
                    j += 2 # next possible flower only on position after the next
                    if n == 0: return True
        return False


if __name__ == "__main__":

    flowerbed = [1, 0, 0, 0, 1]
    # n = 1
    n = 2
    solution = Solution()
    print(solution.canPlaceFlowers(flowerbed, n))
