# O(N) Time Complexity
# O(1) Space Complexity

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prev=0
        minVal,maxVal=0,0
        #min  max initialize
        for i in differences:
            curr=i+prev
            if curr<minVal:
                minVal=curr
            elif curr>maxVal:
                maxVal=curr
            prev=curr
        
        if lower-minVal<=upper-maxVal:
            return (upper-maxVal)-(lower-minVal)+1
        return 0
