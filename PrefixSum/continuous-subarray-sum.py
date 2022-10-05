# O(N) Time Complexity
# O(N) Space Complexity

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum=0
        dic={}
        count=0
        
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
            if nums[i]%k==0:
                count-=1
        
        if count>0:
            return True
        return False
