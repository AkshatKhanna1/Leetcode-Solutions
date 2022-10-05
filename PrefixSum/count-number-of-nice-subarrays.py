# O(N) Time Complexity
# O(N) Space Complexity

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefixSum=0
        dic={}
        count=0
        
        for i in range(len(nums)):
            if nums[i]&1!=0:
                prefixSum+=1
            if prefixSum not in dic:
                dic[prefixSum]=0
            if prefixSum==k:
                count+=1
            if prefixSum-k in dic:
                count+=dic[prefixSum-k]
            dic[prefixSum]+=1

        return count
