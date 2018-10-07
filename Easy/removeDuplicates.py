def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    s = sorted(set(nums))
    nums[:len(s)] = s
    print(nums[:len(s)])
    return len(s)







if __name__ == "__main__":
    nums = [-1,0,0,0,0,3,3]
    removeDuplicates(nums)