"""
Share
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

 

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
 

Note:  1 <= S.length <= 1000
"""
"""
large group 的定义：数组中有若干连续相同子母的子数组，如果子数组的长度大于等于 3，则认为其是 large group。
本题就是返回所有子数组的起始索引和终止索引。

解法：双指针
指定两个指针 i, j，当 j == len(S)-1 或者 S[j] != S[j+1] 的时候，判读是否为 large group
"""
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ans = []
        i = 0
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j + 1
        return ans


if __name__ == "__main__":

    # S = "abbxxxxzzy"  # return [[3, 6]]
    # S = "abc"  # return []
    S = "abcdddeeeeaabbbcd"  # return [[3, 5], [6, 9], [12, 14]]
    solution = Solution()
    print(solution.largeGroupPositions(S))