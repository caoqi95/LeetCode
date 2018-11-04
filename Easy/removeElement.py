class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # solution 1
        while val in nums:
            nums.remove(val)

        print(len(nums))

        ## solution 2
        #for i in range(len(nums),-1,-1):
        #    if nums[i] == val:
        #        nums.pop(i)

        return len(nums)

if __name__ == '__main__':
    nums = [2,2,3,0,4,2]
    val = 2
    solution = Solution()
    solution.removeElement(nums, val)