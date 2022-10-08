# O(N) Time Complexity
# O(1) Space Complexity

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sumRight=0
        for i in nums:
            sumRight+=i
        sumLeft=0
        count=0
        for i in nums[0:-1]:
            sumLeft+=i
            sumRight-=i
            if sumLeft>=sumRight:
                count+=1
        return count
