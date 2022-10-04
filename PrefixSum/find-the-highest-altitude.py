# Time Complexity O(N)
# Space Complexity O(1)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max=0
        sum=0
        for i in gain:
            sum+=i
            if sum>max:
                max=sum
        return max
