class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        insert = 0
        if target in nums:
            insert = nums.index(target)
            print(insert)
            return insert
        elif nums[-1] < target:
            insert = len(nums)
            print(insert)
            return insert
        else:
            for i in range(len(nums)):
                if nums[i]> target :
                    insert = i
                    print(insert)
                    return insert

if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 5
    solution = Solution()
    solution.searchInsert(nums, target)
