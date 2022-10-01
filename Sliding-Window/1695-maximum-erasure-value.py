# O(N) Time Complexity
# O(N) Space Complexity

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s=set()
        currSum=0
        maxSum=0
        start=0
        for i in range(len(nums)):
            if nums[i] in s:
                while nums[i] in s:   
                    currSum-=nums[start]
                    s.remove(nums[start])
                    start+=1
            s.add(nums[i])
            currSum+=nums[i]
            if maxSum<currSum:
                maxSum=currSum
        return maxSum
