#O(N) Time Complexity
#O(1) Space Complexity

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum=0
        n=len(nums)
        for i in range(k):
            sum+=nums[i]
        maxSum=sum
        for i in range(k,n):
            sum=sum+nums[i]-nums[i-k]
            if sum>maxSum:
                maxSum=sum
        return maxSum/k
