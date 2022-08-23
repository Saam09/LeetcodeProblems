class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    nums2=[]
                    nums2.append(i)
                    nums2.append(j)
                    return nums2
                    
