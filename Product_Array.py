class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = [1] * len(nums) 
        
        for i in range(len(nums)):
            m=1
            for j in nums:
                if j - nums[i] != 0:
                    m = m*j
            a[i] = m
        return a
