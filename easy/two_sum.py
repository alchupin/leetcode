# https://leetcode.com/problems/two-sum/description/

def two_sum(nums, target):
    if len(nums) == 2:
        return [0, 1]
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                index_1 = nums.index(nums[i])
                index_2 = nums.index(nums[j], index_1+1,)
                return [index_1, index_2]
    

# leetcode    
def two_sum(nums, target):      
        result = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in result:
                result[num] = i
            else:
                return [result[diff], i]