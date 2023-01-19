class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                    if i != j:
                        x = nums[i] + nums[j]
                        if x == target:
                            a = [i,j]
                            return a
