"""
Given an array A of strings made only from lowercase letters, return a list of all characters 
that show up in all strings within the list (including duplicates).  For example, if a character 
occurs 3 times in all strings but not 4 times, you need to include that character three times 
in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
"""
import collections
import functools

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        def intersect(a,b):
            ans = []
            # count number of chars in a 
            count = collections.Counter(a)
            # we loop through b now
            for ch in b:
                # everytime we encounter a character in b that is present in a too, we add that
                # character to ans array and descrease count for that character by 1.
                # repeat until the count[ch] = 0
                if ch in count and count[ch] != 0:
                    ans.append(ch)
                    count[ch] -= 1
            return ans
        
        return functools.reduce(lambda x, y:intersect(x, y), A)


if __name__ == "__main__":

    # A = ["bella", "label", "roller"]
    A = ["cool", "lock", "cook"]
    solution = Solution()
    print(solution.commonChars(A))