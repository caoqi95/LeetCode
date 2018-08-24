# solution 1
# run time: Time Limit Exceeded
# return a list, [index1,index2]
def twoSum(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if (nums[i] + nums[j] == target):
                #print([i, j])
                return [i, j]
    return [0, 0]




# solution 2
# run time: 1172ms
# return a list, [index1,index2]
def twoSum(nums, target):
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums and nums.index(diff) != i:
            nums[i] = float('nan') # from other's solution
            return [i, nums.index(diff)]




# solusion 3, from other's solution
# run time : 48ms
# return a tuple, (index1, index2)
def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        x = nums[i]
        if target-x in dict:
            print(dict[target-x], i)
            return (dict[target-x], i)
        dict[x] = i

