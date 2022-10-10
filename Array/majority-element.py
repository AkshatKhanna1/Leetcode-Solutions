# O(N) Time Complexity
# O(1) Space 
# It was already mentioned in question that majority element is always present

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        value=0
        for i in nums:
            if value==i:
                count+=1
            else:
                if count==0 or count-1==0:
                    value=i
                    count=1
                else:
                    count-=1
        return value
