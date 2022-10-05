# O(N) Time Complexity
# O(N) Space Complexity

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum=0
        count=0
        dic={}
        for i in range(len(nums)):
            prefixSum+=nums[i]
            rem=prefixSum%k
            if rem not in dic:
                dic[rem]=0
            if rem==0:
                count+=1
            if rem in dic:
                count+=dic[rem]
            dic[rem]+=1
        
        
        return count
