# O(N) Time Complexity
# O(1) Space Complexity

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        k=nums[0]
        for i in range(1,len(nums)):
            nums[i]+=k
            k=nums[i]
        return nums
