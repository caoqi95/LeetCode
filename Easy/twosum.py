# return a tuple, (index1, index2)
def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        x = nums[i]
        if target-x in dict:
            print(dict[target-x], i)
            return (dict[target-x], i)
        dict[x] = i




if __name__ == '__main__':
    twoSum([2,7,11,15], 9)
