# O(N) Time Complexity
# O(1) Space Complexity

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        val=nums[0]
        n=len(nums)

        for i in range(1,n):
            val+=nums[i]
            nums[i]=val

        if nums[n-1]-nums[0]==0:
            return 0

        for i in range(1,n):
            if nums[i-1]==nums[n-1]-nums[i]:
                return i

        return -1
