# O(N) Time Complexity
# O(1) Space Complexity

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n=len(nums)
        val=nums[0]
        min=0
        if val<0:
            min=val
        for i in range(1,n):
            val+=nums[i]
            nums[i]=val
            if val<0 and min>val:
                min=val
        return -1*min+1
