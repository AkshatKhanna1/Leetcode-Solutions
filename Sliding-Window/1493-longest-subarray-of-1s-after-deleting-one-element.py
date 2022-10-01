# O(N) Time Complexity
# O(1) Space Complexity

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count_0=0
        n=len(nums)
        maxSize=0
        currSize=0
        left=0
        for i in range(n):
            currSize+=1
            if nums[i]==0:
                count_0+=1
            if count_0>1:
                while count_0>1 and left<=i:
                    if nums[left]==0:
                        count_0-=1
                    currSize-=1
                    left+=1
            if currSize>maxSize and count_0<=1:
                maxSize=currSize
        return maxSize-1
