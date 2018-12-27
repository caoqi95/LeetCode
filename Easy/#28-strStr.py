class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except ValueError:
            return -1

if __name__ == '__main__':
   haystack ='hello'
   needle = 'll'
   solution = Solution()
   solution.strStr(haystack, needle)