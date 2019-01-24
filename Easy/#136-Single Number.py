# coding=utf-8
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        # 自己的解法：太慢了
        d = {}
        for n in nums:
            c = nums.count(n)
            d[n] = c

        for i in d.values():
            if i == 1:
                print(list(d.keys())[list(d.values()).index(i)])
                return list(d.keys())[list(d.values()).index(i)]
        

        # leetcode 解法一：数学法 2∗(a+b+c)−(a+a+b+b+c)=c，运行时间少
        print(2 * sum(set(nums)) - sum(set(nums)))
        return 2 * sum(set(nums)) - sum(set(nums))
        
       

        # leetcode 解法二：列表操作，耗时长
        no_list = []
        for i in nums:
            if i not in no_list:
                no_list.append(i)
            else:
                no_list.remove(i)
        print(no_list.pop())
        #return no_list.pop()
         """

        # leetcode 解法三：哈希表，待研究
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = i

        # print(hash_table.popitem()[0])
        return hash_table.popitem()[0]





if __name__ == '__main__':

    nums = [1, 0, 1]
    # nums = [2, 2, 1]
    # nums = [4, 1, 2, 1, 2, 3, 3]
    solution = Solution()
    solution.singleNumber(nums)