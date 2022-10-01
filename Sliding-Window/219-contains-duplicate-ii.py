# O(N) Time Complexity
# O(min(N,K)) Space Complexity
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        s=set()
        for i in range(min(k+1,n)):
            if nums[i] in s:
                return True
            s.add(nums[i])
        for i in range(k+1,n,1):
            s.remove(nums[i-k-1])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False   
