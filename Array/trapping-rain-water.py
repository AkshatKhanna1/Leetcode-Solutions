# O(N) Time Complexity
# O(1) Space Complexity

class Solution:
    def trap(self, height: List[int]) -> int:
        
        n=len(height)
        waterTrapped=0
        maxVal=height[0]
        maxIdx=0
        
        for i in range(1,n):
            if height[i]>maxVal:
                maxVal=height[i]
                maxIdx=i
                
        leftMax=height[0]
        
        for i in range(1,maxIdx):
            if min(maxVal,leftMax)>height[i]:
                waterTrapped+=min(maxVal,leftMax)-height[i]
            if height[i]>leftMax:
                leftMax=height[i]
         
        rightMax=height[-1]
        
        for i in range(n-2,maxIdx,-1):
            if min(maxVal,rightMax)>height[i]:
                waterTrapped+=min(maxVal,rightMax)-height[i]
            if height[i]>rightMax:
                rightMax=height[i]
        
        return waterTrapped
        
